from app import db

def save(translation):
    db.translations.insert_one(translation)

def get(uid):
    db.translations.find_one({'uid': uid})

def get_by_status(status):
    return db.translations.find({'status': status})
