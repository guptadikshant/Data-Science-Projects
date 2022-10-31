import pymongo
from sensor.constant.database import DATABASE_NAME, MONGODB_URL
import certifi

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                # mongo_db_url = MONGODB_URL
                MongoDBClient.client = pymongo.MongoClient(MONGODB_URL)
            self.client = pymongo.MongoClient(MONGODB_URL)
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
