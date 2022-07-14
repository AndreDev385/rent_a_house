import abc
from typing import Optional


class RoomRepository(abc.ABC):
    @abc.abstractmethod
    def list(self, filters: Optional[dict]):
        pass
