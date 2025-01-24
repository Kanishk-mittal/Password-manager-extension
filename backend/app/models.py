from pymongo import MongoClient

class TestModel:
    def __init__(self, message):
        self.message = message

    def save(self,db):
        db.test_collection.insert_one({"message": self.message})
