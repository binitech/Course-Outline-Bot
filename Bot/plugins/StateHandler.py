#####################################################################################
"""                         HANDLING STATES                                       """
#####################################################################################
from Bot import dp
from Bot.helpers import ManageCourse
from Bot.helpers.Database import CsFile
from aiogram import types
from aiogram.dispatcher import FSMContext
from Bot.helpers.ManageCourse import AddMaterialForm, RemoveMaterialForm, DescEditForm, CourseManager, CrhEditForm, \
    FileIdEditForm, AddNewCourseForm


@dp.message_handler(state=DescEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the description for this course")
        await DescEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=DescEditForm.desc)
async def editDesc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        cs = CourseManager()
        cs.edit_desc(c_code=data['code'], value=message.text)
    await message.answer("Description changed successfully")
    await state.finish()


#########################################################################################


@dp.message_handler(state=CrhEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the Credit hour for this course")
        await CrhEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=CrhEditForm.crh)
async def editDesc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        cs = CourseManager()
        cs.edit_crh(c_code=data['code'], value=message.text)
    await message.answer("Credit hour changed successfully")
    await state.finish()


#########################################################################################


@dp.message_handler(state=FileIdEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the File for this course")
        await FileIdEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=FileIdEditForm.file, content_types=types.message.ContentType.ANY)
async def editDesc(message: types.message.ContentType.ANY, state: FSMContext):
    if message.document:
        async with state.proxy() as data:
            cs = CourseManager()
            cs.edit_fileId(c_code=data['code'], value=message.document.file_id)
        await message.answer("File Id String changed successfully")
        await state.finish()
    else:
        await message.answer("Please send me document file.")

####################################################################################


@dp.message_handler(state=RemoveMaterialForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        func = ManageCourse.listMaterials(message.text)
        await message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")
        await state.finish()
    else:
        await message.answer("The course code you entered is incorrect")

#####################################################################################


@dp.message_handler(state=AddMaterialForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Send me Material Title/Name")
        await AddMaterialForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=AddMaterialForm.cName)
async def removeMaterial(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Please send material\'s Document/File")
    await AddMaterialForm.next()


@dp.message_handler(state=AddMaterialForm.cFile, content_types=types.message.ContentType.ANY)
async def AddMatCFile(message: types.Message, state: FSMContext):
    if message.document:
        async with state.proxy() as data:
            data['fileId'] = message.document.file_id
        NewMaterial = [data['name'], data['fileId']]
        CourseManager().add_material(data['code'], NewMaterial)
        await message.answer("Material Added Successfully!")
        await state.finish()
    else:
        await message.answer("🙂Incorrect Document\nPlease send material\'s Document/File")


@dp.message_handler(state=AddNewCourseForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text not in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Send me Material Title/Name")
        await AddNewCourseForm.next()
    else:
        await message.answer("The course code you entered is available in the courses list")


@dp.message_handler(state=AddNewCourseForm.name)
async def removeMaterial(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        cs = CourseManager()
        cs.add_course(code=data['code'].upper(), name=message.text)
    await message.answer("Course added successfully go and edit details about it.")
    await state.finish()
