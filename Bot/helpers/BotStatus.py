from Bot import bot


def status():
    TEXT = f"Total Bot Users: " \
           f"\nActive Users: " \
           f"\nDead Users: " \
           f"\nTotal Courses: " \
           f"\nTotal Materials: "
    return TEXT


async def log(event):
    TEXT = f"""<b>-----------LOG-----------</b>
🆔 {event.from_user.id} <a href="tg://user?id={event.from_user.id}">( {event.from_user.first_name} )</a>
🤖 {event.from_user.is_bot}
👤 {event.from_user.first_name}
➡️ {event.from_user.last_name}
🌀 @{event.from_user.username}

   <b>{event.text}</b>"""
    await bot.send_message(-619480714, TEXT, parse_mode="HTML")


async def adminLog(event, stat):
    TEXT = f"""<b>-----------ADMIN LOG-----------</b>
    @Binitech
🆔 {event.from_user.id} <a href="tg://user?id={event.from_user.id}">( {event.from_user.first_name} )</a>
🤖 {event.from_user.is_bot}
👤 {event.from_user.first_name}
➡️ {event.from_user.last_name}
🌀 @{event.from_user.username}
        <b>State: {stat}</b>"""
    await bot.send_message(-619480714, TEXT, parse_mode="HTML")
