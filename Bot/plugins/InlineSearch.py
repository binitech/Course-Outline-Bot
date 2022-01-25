import re
import uuid
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedDocument, \
    InlineQuery
from Bot import dp, bot

#####################################################################################
"""                 HANDLING THE INLINE SEARCHING MODE                            """
#####################################################################################
lst = [
    ["Applied Mathematics I", "Math1101",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["General Physics-I", "Phys1101",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["General Chemistry", "Chem1101",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Introduction to Computing", "CSE1101",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Communicative English Skills", "ENG1011",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Civic and Ethical Education", "LAR1011",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Health &Physical Education I", "HPEd1011",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Logic and Critical Thinking", "LAR1012",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Applied Mathematics II", "Math1102",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Emerging Technologies", "Phys1102",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Fundamentals of Programming", "CSE1102",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Engineering Drawing", "DME1102",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ["Basic Writing Skills", "ENG1102",
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Data Structure and Algorithm', 'CSE2101',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Electronic Circuit', 'ECE2101', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Applied Mathematics III', 'MATH2051',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Fundamental of Electrical Engineering', 'PCE2101',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Principle of Economics', 'SOS311', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Object Oriented Programming', 'CSE2202',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Discrete Mathematics for CSE', 'CSE2206',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Digital Logic Design', 'ECE3204', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Database Systems', 'CSE3207', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Electronic circuit II', 'ECE2202', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['System Programming', 'CSE2320', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Computer Graphics', 'CSE3310', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Algorithms', 'CSE3211', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Probability and Random Process', 'ECE3103',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Fund. of software Engineering', 'CSE3205',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Computer Architecture & Organization', 'CSE3203',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Operating System', 'CSE3204', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Data Communication & Computer Networks', 'CSE3221',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Artificial', 'CSE3206',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['SOftware Requirement Engineering', 'CSE3308',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Web Programming', 'CSE3306', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Advanced Programming', 'CSE3312', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Formal Language and automata Theory', 'unknown',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Engineering Research and Development Methodology', 'CSE4221',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Multimedia Tech.', 'CSE4303', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Software Design and Architecture', 'CSE4309',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Mobile Computing and Applications', 'CSE4311',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Signals and Systems', 'ECE2204', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Data mining', 'CSE5317',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to NLP', 'CSE5321', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Computer System and security', 'Unkown',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Programming languages', 'CSE4202', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Project Management', 'CSE4302', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Law', 'Unknown', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Compiler Design', 'CSE4310', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Digital Signal Processing', 'ECE3205',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['VLSI Design', 'ECE5307', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Electrical Network Analysis and synthesis', 'PCE3201',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Computer Vision', 'CSE4312',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Semester Project', 'CSE5201', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Seminar', 'CSE5205', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Distributed Systems', 'CSE5307', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Wireless mobile Networks', 'CSE5309',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Image Processing', 'CSE5311', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Human Computer Interaction', 'CSE5313',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Audio & Video Production', 'CSE5315',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Advanced Network', 'CSE5319', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Control Systems', 'PCE3204',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['B.Sc. Project', 'CSE5202', 'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Entrepreneurship for Engineers', 'SOSC412',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Computer Games & Animation', 'CSE5304',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Special Topics in Computer Science & Engineering', 'CSE5306',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Real time and Embedded Systems', 'CSE5308',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Software Quality & Testing', 'CSE5310',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Computer Ethics and Social Issues', 'CSE5312',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME'],
    ['Introduction to Robotics and Industrial Automation', 'PCE5308',
     'BQACAgQAAxkBAAENfdhh4rifuD5G4PvblNqo-JpkBrj2ZAACJwkAAncsEFN81CMwt3afZyME']]


@dp.inline_handler()
async def inline_starter(inline_handler: InlineQuery):
    """handling the inline searching mode and giving
    filtered list of items for the user according
    to their text input"""

    txt = inline_handler.query or 'No result'
    item = []
    i = 0
    for x in lst:
        if i >= 30:
            break
        i += 1
        for val in range(2):
            if re.search(txt.lower(), x[val].lower()):
                item.append(
                    InlineQueryResultCachedDocument(
                        id=str(uuid.uuid4()),
                        title=x[0],
                        document_file_id=x[2],
                        caption=x[0] or "",
                        description=x[1]
                    )
                )
    if len(item) == 0:
        item.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Oops your search didn't match my course list",
                description="No result",
                input_message_content=InputTextMessageContent("No result")
            )
        )
    await bot.answer_inline_query(inline_handler.id, results=item, cache_time=1)
