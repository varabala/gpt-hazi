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