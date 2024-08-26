""" Gera registros Mockados para cada log """

import random
from faker import Faker
import json
import uuid
import datetime

fake = Faker()


class DataGenerator:
    """ Gera Objetos Mockados para uso no Projeto """

    devices = ["smart_tv", "smartphone", "computer", "tablet"]
    content_types = ["documentary", "serie", "movie", "novel"]
    capitais_brasil = [
                        "Aracaju", "Belém", "Belo Horizonte", "Boa Vista", "Brasília", "Campo Grande", 
                        "Cuiabá", "Curitiba", "Florianópolis", "Fortaleza", "Goiânia", "João Pessoa", 
                        "Macapá", "Maceió", "Manaus", "Natal", "Palmas", "Porto Alegre", 
                        "Porto Velho", "Recife", "Rio Branco", "Rio de Janeiro", "Salvador", 
                        "São Luís", "São Paulo", "Teresina", "Vitória"
                    ]

    
    @staticmethod
    def log_generator() -> dict:
        """ 
            Gera e retorna um Log Mockado com dados de Acesso 
            de cada usuário.
        """

        access_timestamp  = str( fake.date_between_dates(date_start=datetime.date(2023,1,1), date_end=datetime.date.today()) )


        log = {
                "id": str(uuid.uuid4()), 
                "access_timestamp": access_timestamp, 
                "device": random.choice(DataGenerator.devices), 
                "content_type": random.choice(DataGenerator.content_types), 
                "location": {
                                "country": "Brazil",
                                "city": random.choice(DataGenerator.capitais_brasil)
                            }
            }
        
        return log



if __name__ == "__main__":

    log = DataGenerator.log_generator()    

    print(json.dumps(log, indent=4, ensure_ascii=False))


