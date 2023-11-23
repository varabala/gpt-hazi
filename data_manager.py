# data_manager.py

from pymongo import MongoClient
from recipe import Recept

class DataManager:
    def __init__(self):
        self.client = MongoClient('mongodb_uri')
        self.db = self.client['adatbazis_neve']
        self.collection = self.db['receptek']

    def get_recept_by_ingredients(self, liked, disliked):
        # Implementáld a lekérdezéseket itt
        pass
