from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

user = config['MongoDB']['user']
password = config['MongoDB']['password']

uri = f"mongodb+srv://{user}:{password}@mucimenu.pholujd.mongodb.net/?retryWrites=true&w=majority"



#uri = "mongodb+srv://varabala2:<password>@mucimenu.pholujd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
