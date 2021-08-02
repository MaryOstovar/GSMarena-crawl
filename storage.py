import json
from abc import ABC, abstractmethod

from mongo import MongoDB


class StorageBase(ABC):
    @abstractmethod
    def store(self, *args, **kwargs):
        pass


class MongoStorage(StorageBase):
    def __init__(self):
        self.mongo = MongoDB()

    def store(self, data, collection, *args, **kwargs):
        collection = getattr(self.mongo.database, collection)
        if isinstance(data, list) and len(data) > 1:
            collection.insert_many(data)
        else:
            collection.insert_one(data)






class FileStorage(StorageBase):
    def store(self, data, filename):
        with open(f'link/{filename}.json', 'w') as s:
            s.write(json.dumps(data))
