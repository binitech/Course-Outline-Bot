from config import db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot.helpers import strings
from Bot.helpers.Database import DptFile

courses = db.get().val()['courses']


def collage(lang=0):
    data = DptFile().get()
    div = "\n   ".join(["➖ " + x for x in list(data)])
    TEXT = strings.collageString[lang].format(div)
    btn = InlineKeyboardMarkup()
    for x in list(data):
        btn.add(InlineKeyboardButton(x, callback_data=f"collage_{x}"))
    return TEXT, btn


def schools(par, lang=0):
    data = DptFile().get()
    NewData = data[par]
    if isinstance(NewData, dict):
        div = "\n   ".join(["▪️ " + x for x in list(NewData)])
        TEXT = strings.schoolStrings[lang].format(par, div)
        btn = InlineKeyboardMarkup()
        for x in list(data[par]):
            btn.add(InlineKeyboardButton(x, callback_data=f"school_{par}_{x}"))
        mainMenu = InlineKeyboardButton(strings.mainMenuString[lang], callback_data="course_menu")
        btn.add(InlineKeyboardButton(strings.backBtnString[lang], callback_data=f"course_menu"), mainMenu)
        return TEXT, btn
    else:
        semester(NewData, True)


def division(par, lang=0):
    data = DptFile().get()
    NewData = data[par[0]][par[1]]
    if isinstance(NewData, dict):
        div = "\n   ".join(["▪️ " + x for x in list(NewData)])
        TEXT = strings.divisionStrings[lang].format(par[1], div)
        btn = InlineKeyboardMarkup()
        for x in list(data[par[0]][par[1]]):
            btn.add(InlineKeyboardButton(x, callback_data=f"depart_{par[0]}_{par[1]}_{x}"))
        mainMenu = InlineKeyboardButton(strings.mainMenuString[lang], callback_data="course_menu")
        btn.add(InlineKeyboardButton(strings.backBtnString[lang], callback_data=f"collage_{par[0]}"), mainMenu)
        return TEXT, btn
    else:
        return semester(NewData, inside=True)


def department(par, lang=0):
    data = DptFile().get()
    NewData = data[par[0]][par[1]][par[2]]
    if isinstance(NewData, dict):
        div = "\n   ".join(["▪️ " + x for x in list(NewData)])
        TEXT = strings.departStrings[lang].format(div)
        btn = InlineKeyboardMarkup()
        for x in list(data[par[0]][par[1]][par[2]]):
            btn.add(InlineKeyboardButton(x, callback_data=f"year_{par[0]}_{par[1]}_{par[2]}_{x}"))
        mainMenu = InlineKeyboardButton(strings.mainMenuString[lang], callback_data="course_menu")
        btn.add(InlineKeyboardButton(strings.backBtnString[lang], callback_data=f"school_{par[0]}_{par[1]}"), mainMenu)
        return TEXT, btn
    else:
        return semester(NewData, True)


def year(par, lang=0):
    data = DptFile().get()
    NewData = data[par[0]][par[1]][par[2]][par[3]]
    if isinstance(NewData, dict):
        div = "\n   ".join([x for x in list(NewData)])
        TEXT = strings.yearStrings[lang].format(div)
        btn = InlineKeyboardMarkup()
        for x in list(NewData):
            btn.add(InlineKeyboardButton(x, callback_data=f"semester_{par[0]}_{par[1]}_{par[2]}_{par[3]}_{x}"))
        mainMenu = InlineKeyboardButton(strings.mainMenuString[lang], callback_data="course_menu")
        btn.add(InlineKeyboardButton(strings.backBtnString[lang], callback_data=f"depart_{par[0]}_{par[1]}_{par[2]}"),
                mainMenu)
        return TEXT, btn
    else:
        return semester(NewData, True)


def semester(par, inside=False, lang=0):
    data = DptFile().get()
    if inside:
        NewData = par
    else:
        NewData = data[par[0]][par[1]][par[2]][par[3]][par[4]]
    Menu = InlineKeyboardButton(strings.mainMenuString[lang], callback_data="course_menu")
    if isinstance(NewData, list):
        txt = []
        for x in NewData:
            txt.append(x[0] + "\n/GetCs_" + x[1].upper())
        div = "\n\n".join(txt)
        courseText = ["Courses: \n\n{}", "ኮርሶች: \n\n{}"]
        TEXT = courseText[lang].format(div)
        mainMenu = InlineKeyboardMarkup()
        if not inside:
            mainMenu.add(InlineKeyboardButton(
                strings.backBtnString[lang],
                callback_data=f"year_{par[0]}_{par[1]}_{par[2]}_{par[3]}"))
        mainMenu.insert(Menu)
        return TEXT, mainMenu
