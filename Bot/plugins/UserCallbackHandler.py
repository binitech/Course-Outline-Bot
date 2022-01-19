from Bot import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from Bot.helpers import courses, materials, strings, buttons
from Bot.helpers.Database import Users, CsFile

dataBase = Users()


@dp.callback_query_handler(Text(equals="course_menu"))
async def courseS(query: types.InlineQuery):
    """handling the course main menu inline button and giving the
    list of collages available"""

    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    func = courses.collage(lang)
    await query.message.answer(func[0], reply_markup=func[1])


@dp.callback_query_handler(Text(startswith="material"))
async def materialHandlerInline(query: types.InlineQuery):
    code = query.data.split("_")[1]
    func = materials.listMaterials(code)
    await query.message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")


@dp.callback_query_handler(Text(startswith="displayMaterial"))
async def displayMaterial(query: types.InlineQuery):
    path = query.data.split('_')
    mat = CsFile().get()[path[1]]['materials'][int(path[2])]
    TEXT = f"*Book Name* : _{mat[0]}_\n\n📚Find More materials : @ASTU\_COBOT"
    await bot.send_document(query.from_user.id,
                            document=mat[1],
                            caption=TEXT, parse_mode="MARKDOWN")


@dp.callback_query_handler(Text(startswith="pageBar"))
async def Pagination(query: types.InlineQuery):
    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    page = query.data.split("_")
    if query.data.startswith("pageBar_back"):
        func = materials.materials(start=int(page[2]), end=int(page[3]), i=int(page[4]), lang=lang)
        await query.message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")
    if query.data.startswith("pageBar_next"):
        func = materials.materials(start=int(page[2]), end=int(page[3]), i=int(page[4]), lang=lang)
        await query.message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")


@dp.callback_query_handler(Text(startswith="lang_"))
async def setLang(query: types.InlineQuery):
    """handling and updating the language by users selection"""

    await query.message.delete()
    userId = query.from_user.id
    if query.data == "lang_english":
        dataBase.set_user_language(userId, 0)
        await query.message.answer("Language settled to english",
                                   reply_markup=buttons.menu(userId))
    if query.data == "lang_amharic":
        dataBase.set_user_language(userId, 1)
        await query.message.answer("ቋንቋ ወደ አማርኛ ተለውጧል",
                                   reply_markup=buttons.menu(userId, 1))


@dp.callback_query_handler(Text(startswith="help_"))
async def helpHandler(query: types.InlineQuery):
    """handling the help desk and giving help to users"""

    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    if query.data == "help_bot":
        await query.message.answer(strings.aboutBot[lang])
    if query.data == "help_admin":
        await query.message.answer(strings.helpAdminText[lang])
    if query.data == "help_number":
        await query.message.answer(strings.helpNumberText[lang], parse_mode="MARKDOWN")


#####################################################################################
"""                             COURSE LISTING SECTION                            """
#####################################################################################


@dp.callback_query_handler(Text(startswith="collage_"))
async def divisionHandler(query: types.InlineQuery):
    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    sc = query.data.split("_")[1]
    func = courses.schools(sc, lang)
    await query.message.answer(func[0], reply_markup=func[1])


@dp.callback_query_handler(Text(startswith="school_"))
async def schoolHandler(query: types.InlineQuery):
    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    sc = query.data.split("_")
    func = courses.division([sc[1], sc[2]], lang)
    await query.message.answer(func[0], reply_markup=func[1])


@dp.callback_query_handler(Text(startswith="depart_"))
async def depHandler(query: types.InlineQuery):
    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    sc = query.data.split("_")
    func = courses.department([sc[1], sc[2], sc[3]], lang)
    await query.message.answer(func[0], reply_markup=func[1])


@dp.callback_query_handler(Text(startswith="year_"))
async def yearHandler(query: types.InlineQuery):
    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    sc = query.data.split("_")
    func = courses.year([sc[1], sc[2], sc[3], sc[4]], lang)
    await query.message.answer(func[0], reply_markup=func[1])


@dp.callback_query_handler(Text(startswith="semester_"))
async def semesterHandler(query: types.InlineQuery):
    await query.message.delete()
    userId = query.from_user.id
    lang = dataBase.get_user_lang(userId)
    sc = query.data.split("_")
    func = courses.semester([sc[1], sc[2], sc[3], sc[4], sc[5]], lang=lang)
    await query.message.answer(func[0], reply_markup=func[1])
