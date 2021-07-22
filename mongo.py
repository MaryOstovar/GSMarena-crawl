from pymongo import MongoClient


class MongoDB:
    instance = None

    # @classmethod
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(*args, **kwargs)
    #     return cls.instance

    def __init__(self):
        self.client = MongoClient()
        self.database = self.client['GSMArena']
