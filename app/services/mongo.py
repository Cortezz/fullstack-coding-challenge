from app import db

def rename_collection(collection, new_collection_name):
    db[collection].rename(new_collection_name)

def delete_collection(collection):
    db[collection].drop()

def collection_empty(collection):
    return db[collection].count() == 0
