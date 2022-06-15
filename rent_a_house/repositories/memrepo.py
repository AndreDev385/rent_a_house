from typing import List
from rent_a_house.domain import room as r


class MemRepo:
    def __init__(self, data: List[dict]):
        self.data = data

    def list(self):
        return [r.Room.from_dict(i) for i in self.data]
