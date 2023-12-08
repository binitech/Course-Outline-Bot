import time
from aiogram import types
from aiogram.utils import exceptions
from Bot import bot


class Admin(object):
    def __init__(self, db):
        self.mailer_status = False
        self.db = db
        self.admins: list = db.get().val()['admins']

    def is_admin(self, user_id) -> bool:
        if user_id in self.admins:
            return True
        else:
            return False

    def add_admin(self, user_id: int) -> bool:
        if self.is_admin(user_id):
            return False
        else:
            self.admins.append(user_id)
            self.db.update({'admins': self.admins})
            return True

    def remove_admin(self, user_id) -> bool:
        if user_id == 362993991:
            return False
        if not self.is_admin(user_id):
            return False
        else:
            self.admins.remove(user_id)
            self.db.update({'admins': self.admins})
            return True

    def get_total_users(self) -> int:
        return len(self.db.child('Users').get().val())

    async def mass_mailer(self, message: types.Message) -> bool:
        self.mailer_status = True
        users = list(self.db.child("Users").get().val())
        bot_message = await bot.send_message(
            message.from_user.id,
            f"Mailing Started \n{self.get_total_users()}Users on Queue"
        )
        blocked = 0
        counter = 0
        while self.mailer_status:
            for user in users:
                try:
                    await bot.send_message(int(user), message)
                except exceptions.BotBlocked:
                    blocked += 1
                counter += 1
                if counter % 20:
                    await bot_message.edit_text(
                        f"Mailed: {counter}\nBlocked: {blocked}"
                    )
                time.sleep(2)
        self.mailer_status = False
        return True

    def stop_mailer(self) -> bool:
        self.mailer_status = False
        return True
