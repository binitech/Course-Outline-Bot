from Bot.helpers.Database import CsFile
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Bot.helpers import strings


def materials(lang=0, start=0, end=10, i=1):
    mat = list(CsFile().get())
    courses = mat[start:end]
    txt = []
    btn = InlineKeyboardMarkup(row_width=5)
    for x in courses:
        txt.append(
            f"*{str(i).zfill(2)}* 🔗 *{CsFile().get()[x]['name']}*\n"
        )
        btn.insert(InlineKeyboardButton(f"{str(i).zfill(2)}", callback_data=f"material_{x}"))
        i += 1
    TEXT = "\n".join(txt)
    TEXT = f"📚Materials\n\n{TEXT}"
    if start >= 10:
        btn.add(InlineKeyboardButton(strings.backBtnString[lang],
                                     callback_data=f"pageBar_back_{start - 10}_{end - 10}_{i - 10 - len(mat)}"))
    if end < len(list(CsFile().get())):
        btn.insert(InlineKeyboardButton(strings.nextBtnString[lang],
                                        callback_data=f"pageBar_next_{start + 10}_{end + 10}_{i}"))
    return TEXT, btn


def listMaterials(code, start=0, end=10, i=1, lang=0):
    mats = CsFile().get()[code]['materials']
    mat = mats[start:end]
    txt = []
    btn = InlineKeyboardMarkup(row_width=5)
    for x in mat:
        txt.append(
            f"*{str(i).zfill(2)}* 🔗 *{x[0]}*"
        )
        btn.insert(InlineKeyboardButton(f"{str(i).zfill(2)}", callback_data=f"displayMaterial_{code}_{i - 1}"))
        i += 1
    if start >= 10:
        btn.add(InlineKeyboardButton(strings.backBtnString[lang],
                                     callback_data=f"listMaterial_back_{start - 10}_{end - 10}_{i - 10 - len(mat)}_{code}"))
    if end < len(mats):
        btn.insert(InlineKeyboardButton(strings.nextBtnString[lang]
                                        , callback_data=f"listMaterial_next_{start + 10}_{end + 10}_{i}_{code}"))
    TEXT = "\n".join(txt)
    TEXT = f"*📕{CsFile().get()[code]['name']}*\n\n{TEXT}"
    return TEXT, btn
