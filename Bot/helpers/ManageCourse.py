from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CourseFile, db
from Bot.helpers.Database import CsFile
from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewCourseForm(StatesGroup):
    code = State()
    name = State()


class DescEditForm(StatesGroup):
    code = State()
    desc = State()


class CrhEditForm(StatesGroup):
    code = State()
    crh = State()


class FileIdEditForm(StatesGroup):
    code = State()
    file = State()


class RemoveMaterialForm(StatesGroup):
    code = State()


class AddMaterialForm(StatesGroup):
    code = State()
    cName = State()
    cFile = State()


class CourseManager:
    def __init__(self):
        self.courses = "courses"

    def edit_desc(self, c_code, value):
        db.child(self.courses).child(c_code).update({"description": value})

    def edit_crh(self, c_code, value):
        db.child(self.courses).child(c_code).update({"crh": value})

    def edit_fileId(self, c_code, value):
        db.child(self.courses).child(c_code).update({"file_id": value})

    def get_material(self, code):
        return db.child(self.courses).child(code).child("materials").get().val()

    def remove_material(self, code, index):
        removedObj = self.get_material(code)
        removedObj.pop(int(index))
        db.child(self.courses).child(code).update({"materials": removedObj})

    def add_material(self, code, value):
        Obj = self.get_material(code)
        Obj.append(value)
        db.child(self.courses).child(code).update({"materials": Obj})

    def add_course(self, code, name):
        data = {
            code: {
                "name": name,
                "code": code,
                "file_id": "BQACAgQAAxkBAAEN4Q5h_Se8R-cPMRGuyubQ72-JiDOpjgACoAkAAld7KFPIdWJ0Hn4oNiME",
                "crh": "3",
                "description": "None available",
                "materials": [
                    [
                        "Test",
                        "BQACAgQAAxkBAAEN4Q5h_Se8R-cPMRGuyubQ72-JiDOpjgACoAkAAld7KFPIdWJ0Hn4oNiME"
                    ]
                ]
            }
        }
        db.child(self.courses).update(data)


def listMaterials(code):
    mat = CsFile().get()[code]['materials']
    i = 1
    txt = []
    btn = InlineKeyboardMarkup(row_width=3)
    for x in mat:
        txt.append(
            f"*{str(i).zfill(2)}* 🔗 *{x[0]}*"
        )
        btn.insert(InlineKeyboardButton(f"{str(i).zfill(2)}", callback_data=f"removeMaterial_{code}_{i - 1}"))
        i += 1
    TEXT = "\n".join(txt)
    TEXT = f"*📕{CourseFile[code]['name']}*\n\n{TEXT}"
    return TEXT, btn
