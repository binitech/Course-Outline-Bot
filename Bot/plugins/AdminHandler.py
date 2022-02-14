from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from Bot import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from Bot.helpers import BotStatus, buttons
from Bot.helpers.BotStatus import adminLog
from Bot.helpers.ManageCourse import AddMaterialForm, RemoveMaterialForm, FileIdEditForm, CrhEditForm, DescEditForm, \
    CourseManager, AddNewCourseForm
from config import admins, db


class AdminForm(StatesGroup):
    id = State()


class RemoveAdmin(StatesGroup):
    id = State()


@dp.message_handler(Text(equals="Admin Panel"))
async def adminPanel(message: types.Message):
    """handling the admin panel and checking if user is an admin"""

    if message.from_user.id in admins:
        await message.answer("Welcome admin", reply_markup=buttons.admin_menu())
    else:
        await message.answer("Nope 😉")


@dp.callback_query_handler(Text(startswith="admin"))
async def admin_panel_callbacks(query: types.InlineQuery):
    """handling the admin panel inline section and provide
    admin functionalities"""

    await query.message.delete()
    if query.data == "admin_menu":
        await bot.send_message(query.from_user.id, "Admin panel", reply_markup=buttons.admin_menu())
    if query.data == "admin_manage":
        adm = '-`'.join([str(x) + '`\n' for x in admins])
        TEXT = f"Manage admin\nadmins list\n\n-`{adm}"
        await bot.send_message(query.from_user.id, TEXT, reply_markup=buttons.admin_subMenu(), parse_mode="MARKDOWN")
    if query.data == "admin_addAdmin":
        await query.message.answer("Enter user id", reply_markup=buttons.cancelBtn)
        await AdminForm.id.set()
    if query.data == "admin_removeAdmin":
        adm = '-`'.join([str(x) + '`\n' for x in admins])
        TEXT = f"Enter id from admins list\n\n-`{adm}"
        await query.message.answer(TEXT, parse_mode="MARKDOWN", reply_markup=buttons.cancelBtn)
        await RemoveAdmin.id.set()

    if query.data == "admin_manage_courses":
        await query.message.answer("Select next move:", reply_markup=buttons.admin_Manage_menu())

    if query.data == "admin_addNewCourse":
        await query.message.answer("Please send course code for the new course", reply_markup=buttons.cancelBtn)
        await AddNewCourseForm.code.set()

    if query.data == "admin_editCourseDesc":
        await DescEditForm.code.set()
        await query.message.answer("Please send me the course code", reply_markup=buttons.cancelBtn)

    if query.data == "admin_editCourseCrh":
        await CrhEditForm.code.set()
        await query.message.answer("Please send me the course code", reply_markup=buttons.cancelBtn)

    if query.data == "admin_editCourseFileId":
        await FileIdEditForm.code.set()
        await query.message.answer("Please send me the course code", reply_markup=buttons.cancelBtn)

    if query.data == "admin_editMaterials":
        await query.message.answer("Select what to do: ", reply_markup=buttons.adminMaterial_Menu())

    if query.data == "admin_removeMaterial":
        await RemoveMaterialForm.code.set()
        await query.message.answer("Send me the course code first", reply_markup=buttons.cancelBtn)

    if query.data == "admin_addMaterial":
        await AddMaterialForm.code.set()
        await query.message.answer("Send me the course code first", reply_markup=buttons.cancelBtn)

    if query.data == "admin_status":
        func = BotStatus.status()
        await query.message.answer(func)


@dp.callback_query_handler(Text(startswith="removeMaterial_"))
async def removeMaterialFinal(query: types.InlineQuery):
    codes = query.data.split("_")
    manager = CourseManager()
    manager.remove_material(codes[1], codes[2])
    await query.message.answer("Successfully removed!")


@dp.message_handler(state=AdminForm.id)
async def adminState(message: types.Message, state: FSMContext):
    if message.text == '/cancel':
        await message.answer("Process cancelled")
        await state.finish()
    elif message.text.isdigit():
        await message.answer(f"added {message.text} to admins list")
        admins.append(int(message.text))
        db.update({"admins": admins})
        stat = f'Added {message.text} as an admin'
        await adminLog(message, stat)
        await state.finish()
    else:
        await message.answer("User id must be number please enter again")


@dp.message_handler(state=RemoveAdmin.id)
async def removeAdmin(message: types.Message, state: FSMContext):
    if message.text == '/cancel':
        await message.answer("Process cancelled")
        await state.finish()
    elif int(message.text) in admins:
        await message.answer(f"removed {message.text} from admins list")
        admins.remove(int(message.text))
        db.update({"admins": admins})
        stat = f'Removed {message.text} from admin list'
        await adminLog(message, stat)
        await state.finish()
    else:
        await message.answer("Invalid admin id please enter again")
