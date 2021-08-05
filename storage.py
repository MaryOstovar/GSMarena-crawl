import json
from abc import ABC, abstractmethod

from mongo import MongoDB


class StorageBase(ABC):
    @abstractmethod
    def store(self, *args, **kwargs):
        pass

    @abstractmethod
    def load(self, *args, **kwargs):
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

    def load(self, collection_name, filter_data):
        collection = self.mongo.database[collection_name]
        if filter_data is not None:
            data = collection.find(filter_data)
        else:
            data = collection.find()
        return data

    def update_flag(self, link):
        self.mongo.database.mobile_links.find_one_and_update(
            {'_id': link['_id']},
            {'$set': {'flag': True}}

        )



class FileStorage(StorageBase):
    def store(self, data, filename):
        with open(f'link/data/{filename}.json', 'w') as s:
            s.write(json.dumps(data))

    def load(self,filename, *args, **kwargs):
        with open(f'link/{filename}.json')as f:
            links = json.loads(f.read())
        return links
