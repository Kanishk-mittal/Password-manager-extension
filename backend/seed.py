from app.models import TestModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
database = client[os.getenv("DB_NAME")]


def seed_data():
    # Using Flask's mongo instance attached to app
    test_model = TestModel("Hello, World!")
    test_model.save(database)

    print("Data seeded successfully!")

seed_data()
