#####################################################################################
"""                         HANDLING STATES                                       """
#####################################################################################
from Bot import dp
from Bot.helpers import ManageCourse
from Bot.helpers.BotStatus import adminLog
from Bot.helpers.Database import CsFile
from aiogram import types
from Bot.helpers.buttons import cancelBtn, menu
from aiogram.dispatcher import FSMContext
from Bot.helpers.ManageCourse import AddMaterialForm, RemoveMaterialForm, DescEditForm, CourseManager, CrhEditForm, \
    FileIdEditForm, AddNewCourseForm


@dp.message_handler(state=DescEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled")
        await state.finish()
    elif message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the description for this course", reply_markup=cancelBtn)
        await DescEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=DescEditForm.desc)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    else:
        async with state.proxy() as data:
            cs = CourseManager()
            cs.edit_desc(c_code=data['code'], value=message.text)
        stat = f"Changed course description of {data['code']} to \n{message.text}"
        await adminLog(message, stat)
        await message.answer("Description changed successfully", reply_markup=menu(message.from_user.id))
        await state.finish()


#########################################################################################


@dp.message_handler(state=CrhEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the Credit hour for this course", reply_markup=cancelBtn)
        await CrhEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=CrhEditForm.crh)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    else:
        async with state.proxy() as data:
            cs = CourseManager()
            cs.edit_crh(c_code=data['code'], value=message.text)
        await message.answer("Credit hour changed successfully", reply_markup=menu(message.from_user.id))
        stat = f'Changed course chr for {data["code"]} to {message.text}'
        await adminLog(message, stat)
        await state.finish()


#########################################################################################


@dp.message_handler(state=FileIdEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the File for this course", reply_markup=cancelBtn)
        await FileIdEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=FileIdEditForm.file, content_types=types.message.ContentType.ANY)
async def editDesc(message: types.message.ContentType.ANY, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.document:
        async with state.proxy() as data:
            cs = CourseManager()
            cs.edit_fileId(c_code=data['code'], value=message.document.file_id)
        await message.answer("File changed successfully", reply_markup=menu(message.from_user.id))
        stat = f'Changed course File for {data["code"]} to {message.document.file_id}'
        await adminLog(message, stat)
        await state.finish()
    else:
        await message.answer("Please send me document file.", reply_markup=cancelBtn)

####################################################################################


@dp.message_handler(state=RemoveMaterialForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.text in list(CsFile().get()):
        func = ManageCourse.listMaterials(message.text)
        await message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")
        await state.finish()
    else:
        await message.answer("The course code you entered is incorrect", reply_markup=cancelBtn)

#####################################################################################


@dp.message_handler(state=AddMaterialForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Send me Course Title/Name", reply_markup=cancelBtn)
        await AddMaterialForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=AddMaterialForm.cName)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    else:
        async with state.proxy() as data:
            data['name'] = message.text
        await message.answer("Please send material\'s Document/File", reply_markup=cancelBtn)
        await AddMaterialForm.next()


@dp.message_handler(state=AddMaterialForm.cFile, content_types=types.message.ContentType.ANY)
async def AddMatCFile(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.document:
        async with state.proxy() as data:
            data['fileId'] = message.document.file_id
        NewMaterial = [data['name'], data['fileId']]
        CourseManager().add_material(data['code'], NewMaterial)
        await message.answer("Material Added Successfully!", reply_markup=menu(message.from_user.id))
        stat = f'Added material for {data["code"]} \nNamed: {data["name"]}'
        await adminLog(message, stat)
        await state.finish()
    else:
        await message.answer("🙂Incorrect Document\nPlease send material\'s Document/File", reply_markup=cancelBtn)


@dp.message_handler(state=AddNewCourseForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    elif message.text not in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Send me Course Title/Name", reply_markup=cancelBtn)
        await AddNewCourseForm.next()
    else:
        await message.answer("The course code you entered is available in the courses list")


@dp.message_handler(state=AddNewCourseForm.name)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text == '🚫Cancel':
        await message.answer("Process cancelled", reply_markup=menu(message.from_user.id))
        await state.finish()
    else:
        async with state.proxy() as data:
            data['name'] = message.text
            cs = CourseManager()
            cs.add_course(code=data['code'].upper(), name=message.text)
        await message.answer("Course added successfully go and edit details about it.",
                             reply_markup=menu(message.from_user.id))
        stat = f'Added new course {data["code"]}'
        await adminLog(message, stat)
        await state.finish()
