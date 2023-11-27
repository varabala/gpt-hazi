from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser
import re

class DataManager:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        user = config['MongoDB']['user']
        password = config['MongoDB']['password']
        uri = f"mongodb+srv://{user}:{password}@mucimenu.pholujd.mongodb.net/?retryWrites=true&w=majority"

        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client['receptek']  # Az adatbázis neve
        self.collection = self.db['gpt-hazi']  # A kollekció neve

    def get_recept_by_ingredients(self, liked, disliked):
        # Implementáld a lekérdezéseket itt
        pass
