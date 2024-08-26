""" MongoDB Atlas Connection Client """

import os
from dotenv import load_dotenv
import logging

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Setup Log
logging.basicConfig(
    encoding='utf-8',    
    filemode="w",
    level= logging.INFO    
)

logger    = logging.getLogger(__name__)
handler   = logging.FileHandler('test.log')
formatter = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


load_dotenv()



class MongoDB:
    """ Gerencia e configura integração com o MongoDB Atlas """


    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
    MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

    @staticmethod
    def get_mongodb_client() -> MongoClient:
        """ Generate and return MongoDB Client """

        print(MongoDB.MONGO_CLUSTER)
        uri = f"mongodb+srv://{MongoDB.MONGO_USERNAME}:{MongoDB.MONGO_PASSWORD}@{MongoDB.MONGO_CLUSTER}.voi2v.mongodb.net/?retryWrites=true&w=majority&appName={MongoDB.MONGO_CLUSTER}"
         
        
        print("uri: ", uri)
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            logger.info("Conexão realizada com Sucesso no MongoDB Atlas")

            return client
        except Exception as e:
           logger.error('Error: ', e)



if __name__ == "__main__":

    MongoDB.get_mongodb_client()
  




