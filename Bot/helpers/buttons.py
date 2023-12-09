from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from config import admins
from Bot.helpers import strings


def menu(uid, lang=0):
    btn1 = KeyboardButton(strings.coursesBtn[lang])
    btn2 = KeyboardButton(strings.aboutBtn[lang])
    # btn3 = KeyboardButton(strings.materialsBtn[lang])
    btn3 = KeyboardButton(strings.askBtn[lang])
    btn4 = KeyboardButton(strings.languageBtn[lang])
    btn5 = KeyboardButton(strings.searchBtn[lang])
    btn6 = KeyboardButton(strings.helpdeskBtn[lang])
    menu1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu1.add(btn1, btn2, btn3, btn4).add(btn5).add(btn6)
    if uid in admins:
        menu1.add(KeyboardButton("Admin Panel"))
    return menu1


def helpDesk(lang=0):
    aboutT = ["About Bot", "ስለ ቦት"]
    getnT = ["Get Numbers", "ቁጥሮች ለማግኘት"]
    helpAT = ["Help Admin", "Admin ለመርዳት"]
    btn1 = InlineKeyboardButton(aboutT[lang], callback_data="help_bot")
    btn2 = InlineKeyboardButton(getnT[lang], callback_data="help_number")
    btn3 = InlineKeyboardButton(helpAT[lang], callback_data="help_admin")
    return InlineKeyboardMarkup().add(btn1, btn3).add(btn2)


def admin_menu():
    btn1 = InlineKeyboardButton("Manage admins", callback_data="admin_manage")
    btn2 = InlineKeyboardButton("Manage Courses", callback_data="admin_manage_courses")
    btn3 = InlineKeyboardButton("Bot Status", callback_data="admin_status")
    return InlineKeyboardMarkup(row_width=2).add(btn1, btn2).insert(btn3)


def admin_Manage_menu():
    btn = InlineKeyboardButton("Add new Course", callback_data="admin_addNewCourse")
    btn1 = InlineKeyboardButton("Edit Course Description", callback_data="admin_editCourseDesc")
    btn2 = InlineKeyboardButton("Edit Course Credit Hour", callback_data="admin_editCourseCrh")
    btn3 = InlineKeyboardButton("Edit Course Outline", callback_data="admin_editCourseFileId")
    btn4 = InlineKeyboardButton("Edit Materials", callback_data="admin_editMaterials")
    return InlineKeyboardMarkup().add(btn).add(btn1).add(btn2).add(btn3).add(btn4)


def adminMaterial_Menu():
    btn1 = InlineKeyboardButton("Add Material", callback_data="admin_addMaterial")
    btn2 = InlineKeyboardButton("Remove Material", callback_data="admin_removeMaterial")
    return InlineKeyboardMarkup().add(btn2, btn1)


def admin_subMenu():
    btn1 = InlineKeyboardButton("Add Admin", callback_data="admin_addAdmin")
    btn2 = InlineKeyboardButton("Remove Admin", callback_data="admin_removeAdmin")
    btn3 = InlineKeyboardButton("Back", callback_data="admin_menu")
    return InlineKeyboardMarkup(row_width=2).add(btn1, btn2, btn3)


def selectLanguage(lang=0):
    TEXT = ["Please select language", "እባክዎ ቋንቋ ይምረጡ"]
    btn = InlineKeyboardButton("English 🇺🇸", callback_data="lang_english")
    btn1 = InlineKeyboardButton("Amharic 🇪🇹", callback_data="lang_amharic")
    mainBtn = InlineKeyboardMarkup().add(btn, btn1)
    return TEXT[lang], mainBtn


cancelBtn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(KeyboardButton("🚫Cancel"))
