from app import db

def save(translation):
    db.translations.insert_one(translation)

def get(uid):
    db.translations.find_one({'uid': uid})
