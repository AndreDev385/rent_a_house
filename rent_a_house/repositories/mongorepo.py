import pymongo

from rent_a_house.domain.room import Room
from rent_a_house.adapters.room_repository import RoomRepository


class MongoRepo(RoomRepository):
    def __init__(self, connection_data) -> None:
        client = pymongo.MongoClient(
            host=connection_data["host"],
            username=connection_data["user"],
            password=connection_data["password"],
            authSource="admin",
        )

        self.db = client[connection_data["dbname"]]

    def list(self, filters=None):
        collection = self.db.rooms
        if filters is None:
            result = collection.find()
        else:
            mongo_filter = {}
            for key, value in filters.items():
                key, operator = key.split("__")
                filter_value = mongo_filter.get(key, {})
                if key == "price":
                    value = int(value)
                filter_value["${}".format(operator)] = value
                mongo_filter[key] = filter_value
            result = collection.find(mongo_filter)
        return [Room.from_dict(d) for d in result]
