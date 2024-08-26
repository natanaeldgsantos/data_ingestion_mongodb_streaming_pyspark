""" MongoDB Data Bulkloader """


from mongodb.client import MongoDB
from log_generator.mock import DataGenerator
import os
import logging

logging.basicConfig(
    filename= "logs/log.log",
    filemode="w",
    encoding='utf-8',
    format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


class DataUploader:
    """ Orquestra e executa todo processo de ingestão de Dados no MongoDB Atlas """


    def __init__(self) -> None:        
        self.database_name = os.getenv("MONGO_CLUSTER")
        self.collection_name = os.getenv("MONGO_COLLECTION")


    def execute_workflow(self) -> None:
        """ Método principal """

        mongo_client = MongoDB.get_mongodb_client()
        database = mongo_client[self.database_name]
        collection = database[self.collection_name]



        for i in range(50):
            
            log = DataGenerator.log_generator()
            response = collection.insert_one(log)
            
        
        mongo_client.close()

if __name__ == "__main__":

    DataUploader().execute_workflow()

    logging.info("Processo de ingestão realizado com sucesso")

            





