import json
from abc import ABC, abstractmethod


class StorageBase(ABC):
    @abstractmethod
    def store(self, *args, **kwargs):
        pass


class MongoStorage(StorageBase):
    def store(self, *args, **kwargs):
        pass


class FileStorage(StorageBase):
    def store(self, data, filename):
        with open(f'link/{filename}.json', 'w') as s:
            s.write(json.dumps(data))
