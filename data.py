from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser

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
'''print(db.list_collection_names())
for doc in collection.find({}):
    print(doc)

print(list(collection.find({})))'''

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

ingredients = ["chicken"]

disliked_ingredients = ['paprika']


query = {
    "$and": [
        {"Ingredients": {"$in": ingredients}},
        {"Ingredients": {"$nin": disliked_ingredients}}
    ]
}
query = {
    "ingredients": {
        "$in": ingredients
    },
    "$not": {
        "ingredients": {
            "$in": disliked_ingredients
        }
    }
}

# A találatok lekérése
results = recipes.find(query)

# A találatok megjelenítése
for result in results:
    print(result)
