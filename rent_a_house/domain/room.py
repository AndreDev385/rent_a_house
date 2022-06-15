from uuid import UUID


class Room:
    def __init__(
        self, code: UUID, size: int, price: float, longitude: float, latitude: float
    ) -> None:
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, adict) -> "Room":
        return cls(
            code=adict["code"],
            size=adict["size"],
            price=adict["price"],
            longitude=adict["longitude"],
            latitude=adict["latitude"],
        )

    def to_dict(self) -> object:
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    def __eq__(self, __o: "Room") -> bool:
        return self.to_dict() == __o.to_dict()
