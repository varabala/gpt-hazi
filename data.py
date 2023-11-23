from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

user = config['MongoDB']['user']
password = config['MongoDB']['password']

uri = f"mongodb+srv://{user}:{password}@mucimenu.pholujd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['gpt-hazi']
collection = db['receptek']
"""

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""

class Recept:
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


recept = Recept(
    id=1,
    title="Crispy Salt and Pepper Potatoes",
    instructions="Preheat oven to 400°F and line a rimmed baking sheet with parchment...",
    image_name="crispy-salt-and-pepper-potatoes.jpg",
    ingredients=["2 large egg whites", "1 pound new potatoes"]
)

recept.display()
