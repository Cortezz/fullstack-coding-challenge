from app import db

def save(translation):
    db.translations.insert_one(translation)

def get(uid):
    db.translations.find_one({'uid': uid})

def get_by_status(status):
    return db.translations.find({'status': status})

def get_by_not_status(status):
    return db.translations.find({'status': { "$ne": 'completed'}})

def update(translation):
    db.translations.find_one_and_replace({'uid': translation['uid']}, translation)
