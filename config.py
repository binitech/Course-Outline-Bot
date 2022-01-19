import pyrebase

API_TOKEN = "Your Token"

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": '',
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}
db = pyrebase.initialize_app(firebaseConfig).database()

admins = db.get().val()["admins"]

CourseFile = db.child("courses").get().val()