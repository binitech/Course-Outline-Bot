from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Bot import bot
from Bot.helpers import strings
from Bot.helpers.Database import CsFile


def list_exams(code, start=0, end=10, i=1, lang=0):
    mats = CsFile().get()[code]['exams']
    mat = mats[start:end]
    txt = []
    btn = InlineKeyboardMarkup(row_width=5)
    for x in mat:
        txt.append(
            f"<b>{str(i).zfill(2)}</b> 🔗 <b>{x[0]}</b>"
        )
        btn.insert(InlineKeyboardButton(f"{str(i).zfill(2)}", callback_data=f"displayExam_{code}_{i - 1}"))
        i += 1
    if start >= 10:
        btn.add(InlineKeyboardButton(strings.backBtnString[lang],
                                     callback_data=f"listExam_back_{start - 10}_{end - 10}_{i - 10 - len(mat)}_{code}"))
    if end < len(mats):
        btn.insert(InlineKeyboardButton(strings.nextBtnString[lang]
                                        , callback_data=f"listExam_next_{start + 10}_{end + 10}_{i}_{code}"))
    TEXT = "\n".join(txt)
    text = f'➖➖ <b>📝Previous Year Exams</b> ➖➖\n\n<b>Name:</b> {CsFile().get()[code]["name"]}' \
           f'\n\n{TEXT}\n\n📚Find More from : @ASTU_COBOT'
    return text, btn


async def display_exam(uid):
    ch = -1001655193585
    await bot.copy_message(uid, ch, 8)
