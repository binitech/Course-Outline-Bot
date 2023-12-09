#####################################################################################
"""                             HELP DESK STRINGS                                 """
#####################################################################################
aboutBot = ["""About Bot
[📖Courses] You can get course details according to your
collage, division, school, year and department on this section.

[👥About] On this section the developer of the bot and functionality are placed.

[📚Materials] You can find materials available for courses on this section.

[⚙️Setting] You can customize the bot language on the setting section.

[🔎Search Course] The main function of the bot, You can search any course on any chat on inline mode
    How?  1)Type @ASTU_COBOT and enter course you want to search
          2)Click the result of your course and you can get the course outline sent to the chat.

[🆘Help Desk] You already here 😅
""", """About Bot
[📖Courses] You can get course details according to your
collage, division, school, year and department on this section.

[👥About] On this section the developer of the bot and functionality are placed.

[📚Materials] You can find materials available for courses on this section.

[⚙️Setting] You can customize the bot language on the setting section.

[🔎Search Course] The main function of the bot, You can search any course on any chat on inline mode
    How?  1)Type @ASTU_COBOT and enter course you want to search
          2)Click the result of your course and you can get the course outline sent to the chat.

[🆘Help Desk] You already here 😅
"""]

helpAdminText = ["[Help Admin]\n\nGIve me start on this project going to "
                 "the github page and freely contribute what ever you want"
                 "\n\nhttps://github.com/binitech/Course-Outline-Bot",
                 "[Help Admin]\n\nGIve me start on this project going to "
                 "the github page and freely contribute what ever you want"
                 "\n\nhttps://github.com/binitech/Course-Outline-Bot"]

helpNumberText = ["[☎️ Get Numbers]\n\n\n*Ambulance:* +251923815901\n\n*CSE Head:* +251221100014\n\n"
                  "*Associate Dean For Academic Affairs:* +251221100026 \n\n"
                  "*Associate Dean For Students Affairs:* +251221100073",
                  "[☎️ ቁጥሮች ለማግኘት]\n\n*አምቡላንስ:* +251923815901\n\n*የCSE ኃላፊ፡* +251221100014\n\n"
                  "* ለአካዳሚክ ጉዳዮች ተባባሪ ዲን፡* +251221100026 \n\n"
                  "*የተማሪዎች ጉዳይ ተባባሪ ዲን፡* +251221100073"
                  ]

#####################################################################################
"""                             MAIN MENU STRINGS                                 """
#####################################################################################
backBtnString = ["🔙 Back", "🔙 ተመለስ"]
nextBtnString = ["➡️ Next", "➡️ ቀጣይ"]
mainMenuString = ["🌐Main Menu", "🌐ዋና ገጽ"]
coursesBtn = ["📖Courses", "📖ኮርሶች"]
aboutBtn = ["👥About", "👥ስለኛ"]
materialsBtn = ["📚Materials", "📚መጻሕፍት"]
askBtn = ["❓Ask Question", "❓ጥያቄ ይጠይቁ"]
languageBtn = ["🗣  Language", "🗣  ቋንቋ"]
searchBtn = ["🔎Search Course", "🔎ኮርስ ፍለጋ"]
helpdeskBtn = ["❔Help Desk", "❔የእገዛ ዴስክ"]


#####################################################################################
"""                             MENU MESSAGE STRINGS                                 """
#####################################################################################

helpButton = ["Hey {}\n\nI'm here to help you please select what you want to get",
              "ሰላም {}\n\nእርስዎን ለመርዳት ዝግጁ ነኝ እባክዎን ማግኘት የሚፈልጉትን ይምረጡ"]

searchButton = ["You can search for course by the course code or the course name"
                "\nClick the below inline button to start search🔎",
                "ኮርሱን በኮርሱ ኮድ ወይም በኮርሱ ስም መፈለግ ይችላሉ። \nፍለጋ🔎 ለመጀመር ከታች ያለውን Inline button ይጫኑ"]

askButton = ["""🌟 Got a question? We're all ears! 🌟 Please send your query now. You can choose from:

✍️ Sending a Text message for quick queries.
📸 Uploading a Photo for visual context.
🎥 Sharing a Video for detailed explanations.
📄 Attaching a Document if you have detailed information or specific documents to share.

Let's get started! 🚀 Your insights are just a message away! send your questions.""", """🌟 ጥያቄ አለህ? 🌟 እባክዎን ጥያቄዎን አሁን ይላኩ። ከሚከተሉት ውስጥ መምረጥ ይችላሉ፡-

✍️ ለፈጣን መጠይቆች የጽሑፍ መልእክት ።
📸 ለእይታ አውድ ፎቶ ።
🎥 ለዝርዝር ማብራሪያ ቪዲዮ ።
📄 ዝርዝር መረጃ ወይም ልዩ ሰነዶች ።

ይላኩልን።"""]

thanksResponse = ["""🌟 Thank you for submitting your question! Our dedicated admins are on the case 🕵️‍♀️ and will work to provide you with an answer as soon as possible. Keep an eye out for a response message coming your way soon! 🚀💬
""", """🌟 ጥያቄህን ስላስገባህ እናመሰግናለን! 🕵️‍♀️  በጉዳዩ ላይ በተቻለ ፍጥነት መልስ ለመስጠት እንሰራለን። በቅርቡ ወደ እርስዎ የሚመጣ የምላሽ መልእክት ይከታተሉ! 🚀💬"""]


#####################################################################################
"""                             COURSE LIST STRINGS                               """
#####################################################################################

collageString = ["Those are collages available in Adama Science and Technology University:"
                 "\n\n   {}\n\nSelect your collage👇",
                 "እነዚህ በአዳማ ሳይንስ እና ቴክኖሎጂ ዩኒቨርሲቲ የሚገኙ ኮሌጅ ናቸው።\n\n   {}\n\nኮሌጅዎን ይምረጡ👇"]

schoolStrings = ["Here are schools available in {}: \n\n   {}\n\nSelect your choice👇",
                 "በ {} ውስጥ የሚገኙ ትምህርት ቤቶች እዚህ አሉ።\n\n   {}\n\nትምህርት ቤትዎን ይምረጡ👇"]

divisionStrings = ["In {} those are the departments: \n\n   {}\n\nSelect your choice👇",
                   "በ {} ውስጥ እነዚህ ክፍሎች ናቸው፡ \n\n   {}\n\nምርጫዎን ይምረጡ👇"]

departStrings = ["This department is 5Years long: \n\n   {}\n\nSelect year to display👇",
                 "ይህ ክፍል 5 አመት ነው፡ \n\n {}\n\nየሚታይበትን አመት ይምረጡ 👇"]

yearStrings = ["Select semester to get courses: \n\n   {}\n\nSelect👇",
               "ኮርሶችን ለማግኘት ሴሚስተር ይምረጡ፡ \n\n {}\n\nይምረጡ👇"]
