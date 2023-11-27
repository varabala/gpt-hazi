from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')

user = config['MongoDB']['user']
password = config['MongoDB']['password']

uri = f"mongodb+srv://{user}:{password}@mucimenu.pholujd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['receptek']
collection = db['gpt-hazi']


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


class Recipe:
    def __init__(self, id, title, instructions, image_name, ingredients):
        self.id = id
        self.title = title
        self.instructions = instructions
        self.image_name = image_name
        self.ingredients = ingredients

    def display(self):
        print(f"Cím: {self.title}")
        print(f"Utasítások: {self.instructions}")
        print("Hozzávalók:")
        for ingredient in self.ingredients:
            print(f" - {ingredient}")




ingredients = []
disliked_ingredients = ['paprika', 'acorn', 'sausage']

results = collection.find({
    "Ingredients": {
        "$all": [re.compile(f".*{ingredient}.*", re.IGNORECASE) for ingredient in ingredients],
        "$nin": [re.compile(f".*{ingredient}.*", re.IGNORECASE) for ingredient in disliked_ingredients]
    }
})

#print(list(results)[0]['Title'])
