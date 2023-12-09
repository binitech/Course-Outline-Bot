from aiogram import types
from aiogram.dispatcher.filters import Text

from Bot import dp, bot
from Bot.helpers import buttons, Database, strings
from config import db, admin_group_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionForm(StatesGroup):
    waiting_for_question = State()


userDb = Database.Users()


async def forward_media_to_admin_group(message, caption, media_type):
    sent_message = None
    if media_type == 'text':
        sent_message = await bot.send_message(admin_group_id, caption)
    elif media_type == 'photo':
        sent_message = await bot.send_photo(admin_group_id, photo=message.photo[-1].file_id, caption=caption)
    elif media_type == 'video':
        sent_message = await bot.send_video(admin_group_id, video=message.video.file_id, caption=caption)
    elif media_type == 'document':
        sent_message = await bot.send_document(admin_group_id, document=message.document.file_id, caption=caption)

    return sent_message.message_id if sent_message else None


async def forward_response_to_user(user_id, response_content, user_message_id):
    if response_content['type'] == 'text':
        await bot.send_message(user_id, response_content['data'], reply_to_message_id=user_message_id)
    elif response_content['type'] == 'photo':
        await bot.send_photo(user_id, photo=response_content['data'], caption=response_content.get('caption', ''),
                             reply_to_message_id=user_message_id)
    elif response_content['type'] == 'video':
        await bot.send_video(user_id, video=response_content['data'], caption=response_content.get('caption', ''),
                             reply_to_message_id=user_message_id)
    elif response_content['type'] == 'document':
        await bot.send_document(user_id, document=response_content['data'], caption=response_content.get('caption', ''),
                                reply_to_message_id=user_message_id)


@dp.message_handler(Text(equals=["❓Ask Question", "❓ጥያቄ ይጠይቁ"]), state="*")
async def ask_question(message: types.Message):
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    await QuestionForm.waiting_for_question.set()
    await message.answer(strings.askButton[lang],
                         reply_markup=buttons.cancelBtn)


@dp.message_handler(content_types=['text', 'photo', 'video', 'document'], state=QuestionForm.waiting_for_question)
async def receive_question(message: types.Message, state: FSMContext):
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=buttons.menu(message.from_user.id, lang))
        await state.finish()
        return
    question_content = {
        'user_id': message.from_user.id,
        'answered': False,
        'caption': message.caption if message.caption else ""
    }

    if message.text:
        question_content['type'] = 'text'
        question_content['data'] = message.text
    elif message.photo:
        question_content['type'] = 'photo'
        question_content['data'] = message.photo[-1].file_id  # Highest quality photo
    elif message.video:
        question_content['type'] = 'video'
        question_content['data'] = message.video.file_id
    elif message.document:
        question_content['type'] = 'document'
        question_content['data'] = message.document.file_id

    # # Forward question to admin group
    caption = f"Question from {message.from_user.username}: " + (
        "(File)" if question_content['type'] != 'text' else question_content['data'])
    if message.caption:
        caption += f"\n\nCaption: {message.caption}"
    caption += "\n\nReply to this message to answer."
    forwarded_message_id = await forward_media_to_admin_group(message, caption, question_content['type'])

    # Store question content along with forwarded message ID in Firebase
    question_content['forwarded_message_id'] = forwarded_message_id
    # Modify the part where you store the question in Firebase
    question_content['user_message_id'] = message.message_id
    db.child("questions").update({forwarded_message_id: question_content})

    await state.finish()
    await message.answer(strings.thanksResponse[lang], reply_markup=buttons.menu(userId, lang))


@dp.message_handler(content_types=['text', 'photo', 'video', 'document'], chat_id=admin_group_id)
async def handle_admin_response(message: types.Message):
    if message.reply_to_message:
        forwarded_message_id = message.reply_to_message.message_id

        # Find the Firebase entry with the matching forwarded_message_id
        question_info = db.child("questions").child(forwarded_message_id).get().val()
        if question_info:
            user_id = question_info['user_id']
            response_content = {
                'caption': message.caption if message.caption else ""
            }

            if message.text:
                response_content['type'] = 'text'
                response_content['data'] = message.text
            elif message.photo:
                response_content['type'] = 'photo'
                response_content['data'] = message.photo[-1].file_id
            elif message.video:
                response_content['type'] = 'video'
                response_content['data'] = message.video.file_id
            elif message.document:
                response_content['type'] = 'document'
                response_content['data'] = message.document.file_id

            # In the handle_admin_response function
            user_message_id = question_info['user_message_id']
            await forward_response_to_user(user_id, response_content, user_message_id)

            # Update Firebase to indicate the question has been answered
            db.child("questions").child(forwarded_message_id).update({"answered": True})
