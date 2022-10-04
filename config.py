import pyrebase
import os
from dotenv import load_dotenv

# loading env configs
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

firebaseConfig = {
    "apiKey": os.getenv('apiKey'),
    "authDomain": os.getenv('authDomain'),
    "databaseURL": os.getenv('databaseURL'),
    "projectId": os.getenv('projectId'),
    "storageBucket": os.getenv('storageBucket'),
    "messagingSenderId": os.getenv('messagingSenderId'),
    "appId": os.getenv('appId'),
    "measurementId": os.getenv('measurementId')
}

db = pyrebase.initialize_app(firebaseConfig).database()

admins = db.get().val()["admins"]

CourseFile = db.child("courses").get().val()
