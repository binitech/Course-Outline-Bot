from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import dp, bot
from Bot.helpers import buttons, Database, courses, materials, strings
from Bot.helpers.BotStatus import log
from Bot.helpers.Database import CsFile

#####################################################################################
"""                        HANDLING THE START COMMAND                             """
#####################################################################################


userDb = Database.Users()


@dp.message_handler(commands=["start"])
async def starter(message: types.Message):
    """Handling start command and storing new users on firebase"""

    await log(message)
    userId = message.from_user.id
    data = {
        "firstName": message.from_user.first_name or "None",
        "lastName": message.from_user.last_name or "None",
        "id": userId,
        "isBot": message.from_user.is_bot,
        "username": message.from_user.username or "None"
    }
    if userDb.is_new(userId):
        userDb.add_user(userId, data)
        func = buttons.selectLanguage()
        await message.answer(
            f"👋Hey {message.from_user.first_name}\nWelcome to ASTU course outline Bot\nPlease select language:",
            reply_markup=func[1])
    else:
        lang = userDb.get_user_lang(userId)
        await message.answer(f"👋Hey {message.from_user.first_name}",
                             reply_markup=buttons.menu(message.from_user.id, lang))


@dp.message_handler(Text(equals=["🗣  Language", "🗣  ቋንቋ"]))
async def settings(message: types.Message):
    """handling language section by both amharic and english
    and updating new language for the user"""

    await log(message)
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    func = buttons.selectLanguage(lang)
    await message.answer(func[0], reply_markup=func[1])


@dp.message_handler(Text(equals=["📖Courses", "📖ኮርሶች"]))
async def courseS(message: types.Message):
    """handling the course listing on both languages
    and providing list of collages available for user
    according to their language selection"""

    await log(message)
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    func = courses.collage(lang)
    await message.answer(func[0], reply_markup=func[1])


@dp.message_handler(Text(equals=["👥About", "👥ስለኛ"]))
async def about(message: types.Message):
    await log(message)
    TEXT = f"[{message.text}]\n\n" \
           f"ASTU Course outline bot\n\n" \
           f"🥷Bot Developer : [вιηι](https://t.me/binitech)" \
           f"\n\nThis bot is fully open-Source feel free to fork and contribute on the project: " \
           f"\nhttps://github.com/binitech/Course-Outline-Bot"
    btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Github", url="https://github.com/binitech/Course-Outline-Bot"))
    await message.answer(TEXT, parse_mode="MARKDOWN", reply_markup=btn)


@dp.message_handler(Text(equals=["📚Materials", "📚መጻሕፍት"]))
async def materialsHandler(message: types.Message):
    """handling the material section and providing
    list of materials for the user"""

    await log(message)
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    func = materials.materials(lang=lang)
    await message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")


@dp.message_handler(Text(equals=["🔎Search Course", "🔎ኮርስ ፍለጋ"]))
async def searchCourse(message: types.Message):
    """handling search course section on both languages and
    giving the user inline button to search using inline mode"""

    await log(message)
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    btnText = ["Start Searching🔎", "መፈለግ ጀምር 🔎"]
    btn = InlineKeyboardMarkup().add(InlineKeyboardButton(btnText[lang], switch_inline_query_current_chat=""))
    await message.answer(strings.searchButton[lang], reply_markup=btn)


@dp.message_handler(Text(equals=["❔Help Desk", "❔የእገዛ ዴስክ"]))
async def HelperDesk(message: types.Message):
    """handling the helping desk on both language and
    provide helping types"""

    await log(message)
    userId = message.from_user.id
    lang = userDb.get_user_lang(userId)
    TEXT = strings.helpButton[lang].format(message.from_user.first_name)
    await message.answer(TEXT, reply_markup=buttons.helpDesk(lang))


@dp.message_handler(Text(startswith="/GetCs_"))
async def GetCourses(message: types.Message):
    """handling the GetCs command which is linked with course code
    and giving the course detail by the course code provided"""
    try:
        cCode = message.text.split("_")[1]
        fullCourse = CsFile().get()[cCode]
        TEXT = f"*Course Name:* _{fullCourse['name']}_\n\n" \
               f"*Course Code:* _{fullCourse['code']}_\n\n" \
               f"*Course credit hour:* _{fullCourse['crh']}_\n\n" \
               f"*About Course:* \n_{fullCourse['description']}_"

        btn = InlineKeyboardMarkup().add(InlineKeyboardButton("📚Materials", callback_data=f'material_{cCode}'))
        await message.answer(TEXT, parse_mode="MARKDOWN", reply_markup=btn)

        Doc_Text = f'➖➖ <b>Course Outline</b> ➖➖\n\n<b>Name:</b> {fullCourse["name"]}' \
                   f'\n<b>Code:</b> {fullCourse["code"]}\n\n📚Find More from : @ASTU_COBOT'

        await bot.send_document(message.from_user.id,
                                document=fullCourse['file_id'],
                                caption=Doc_Text,
                                parse_mode="HTML")
    except:
        await message.answer("Oops😔\n\nCourse detail is not available for now")
