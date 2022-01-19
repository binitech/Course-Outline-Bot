from config import db


class Users(object):
    def __init__(self):
        self.Users = "Users"

    def is_new(self, userid):
        """checking if user is new for the bot or not"""

        if db.child(self.Users).child(userid).get().val() is None:
            return True
        else:
            return False

    def add_user(self, userid, data):
        db.child(self.Users).child(userid).set(data)

    def set_user_language(self, userid, lang):
        db.child(self.Users).child(userid).update({"lang": lang})

    def get_user_lang(self, userid):
        return db.child(self.Users).child(userid).get().val()["lang"]

    def get_total_users(self):
        return len(db.child(self.Users).get().val())


class CsFile:
    def __init__(self):
        self.course = "courses"

    def get(self):
        return db.child(self.course).get().val()
