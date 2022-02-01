import re
import uuid
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedDocument, \
    InlineQuery
from Bot import dp, bot
from Bot.helpers.Database import CsFile

#####################################################################################
"""                 HANDLING THE INLINE SEARCHING MODE                            """
#####################################################################################
lst = [
    ["Applied Mathematics I", "Math1101",
     ],
    ["General Physics-I", "Phys1101",
     ],
    ["General Chemistry", "Chem1101",
     ],
    ["Introduction to Computing", "CSE1101",
     ],
    ["Communicative English Skills", "ENG1011",
     ],
    ["Civic and Ethical Education", "LAR1011",
     ],
    ["Health &Physical Education I", "HPEd1011",
     ],
    ["Logic and Critical Thinking", "LAR1012",
     ],
    ["Applied Mathematics II", "Math1102",
     ],
    ["Emerging Technologies", "Phys1102",
     ],
    ["Fundamentals of Programming", "CSE1102",
     ],
    ["Engineering Drawing", "DME1102",
     ],
    ["Basic Writing Skills", "ENG1102",
     ],
    ['Data Structure and Algorithm', 'CSE2101',
     ],
    ['Electronic Circuit', 'ECE2101'],
    ['Applied Mathematics III', 'MATH2051',
     ],
    ['Fundamental of Electrical Engineering', 'PCE2101',
     ],
    ['Principle of Economics', 'SOS311'],
    ['Object Oriented Programming', 'CSE2202',
     ],
    ['Discrete Mathematics for CSE', 'CSE2206',
     ],
    ['Digital Logic Design', 'ECE3204'],
    ['Database Systems', 'CSE3207'],
    ['Electronic circuit II', 'ECE2202'],
    ['System Programming', 'CSE2320'],
    ['Computer Graphics', 'CSE3310'],
    ['Algorithms', 'CSE3211'],
    ['Probability and Random Process', 'ECE3103',
     ],
    ['Fund. of software Engineering', 'CSE3205',
     ],
    ['Computer Architecture & Organization', 'CSE3203',
     ],
    ['Operating System', 'CSE3204'],
    ['Data Communication & Computer Networks', 'CSE3221',
     ],
    ['Introduction to Artificial', 'CSE3206',
     ],
    ['SOftware Requirement Engineering', 'CSE3308',
     ],
    ['Web Programming', 'CSE3306'],
    ['Advanced Programming', 'CSE3312'],
    ['Formal Language and automata Theory', 'unknown',
     ],
    ['Engineering Research and Development Methodology', 'CSE4221',
     ],
    ['Multimedia Tech.', 'CSE4303'],
    ['Software Design and Architecture', 'CSE4309',
     ],
    ['Mobile Computing and Applications', 'CSE4311',
     ],
    ['Signals and Systems', 'ECE2204'],
    ['Introduction to Data mining', 'CSE5317',
     ],
    ['Introduction to NLP', 'CSE5321'],
    ['Computer System and security', 'Unkown',
     ],
    ['Programming languages', 'CSE4202'],
    ['Project Management', 'CSE4302'],
    ['Introduction to Law', 'Unknown'],
    ['Compiler Design', 'CSE4310'],
    ['Digital Signal Processing', 'ECE3205',
     ],
    ['VLSI Design', 'ECE5307'],
    ['Electrical Network Analysis and synthesis', 'PCE3201',
     ],
    ['Introduction to Computer Vision', 'CSE4312',
     ],
    ['Semester Project', 'CSE5201'],
    ['Seminar', 'CSE5205'],
    ['Distributed Systems', 'CSE5307'],
    ['Wireless mobile Networks', 'CSE5309',
     ],
    ['Image Processing', 'CSE5311'],
    ['Human Computer Interaction', 'CSE5313',
     ],
    ['Introduction to Audio & Video Production', 'CSE5315',
     ],
    ['Advanced Network', 'CSE5319'],
    ['Introduction to Control Systems', 'PCE3204',
     ],
    ['B.Sc. Project', 'CSE5202'],
    ['Entrepreneurship for Engineers', 'SOSC412', ],
    ['Computer Games & Animation', 'CSE5304',
     ],
    ['Special Topics in Computer Science & Engineering', 'CSE5306',
     ],
    ['Real time and Embedded Systems', 'CSE5308',
     ],
    ['Software Quality & Testing', 'CSE5310',
     ],
    ['Computer Ethics and Social Issues', 'CSE5312',
     ],
    ['Introduction to Robotics and Industrial Automation', 'PCE5308',
     ]]


@dp.inline_handler()
async def inline_starter(inline_handler: InlineQuery):
    """handling the inline searching mode and giving
    filtered list of items for the user according
    to their text input"""

    item = []
    txt = inline_handler.query or None
    if txt is None:
        item.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Start Typing course name or course code",
                description="No result",
                input_message_content=InputTextMessageContent("No result")
            )
        )
    else:
        i = 0
        cs = CsFile().get()
        for x in lst:
            if i >= 30:
                break
            i += 1
            for val in range(2):
                if re.search(txt.lower(), x[val].lower()):
                    txt = f'➖➖ <b>Course Outline</b> ➖➖\n\n<b>Name:</b> {x[0]}' \
                       f'\n<b>Code:</b> {x[1]}\n\n📚Find More from : @ASTU_COBOT'
                    item.append(
                        InlineQueryResultCachedDocument(
                            id=str(uuid.uuid4()),
                            title=x[0],
                            document_file_id=cs[x[1].upper()]['file_id'],
                            caption=txt,
                            description=x[1],
                            parse_mode="HTML"
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
