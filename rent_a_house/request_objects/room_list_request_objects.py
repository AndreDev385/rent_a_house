from typing import Mapping, Optional


class InvalidRequestObject:
    def __init__(self) -> None:
        self.errors = []

    def add_error(self, parameter: str, message: str):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self) -> bool:
        return False


class ValidRequestObject:
    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError

    def __bool__(self) -> bool:
        return True


class RoomListRequestObject(ValidRequestObject):
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]

    def __init__(self, filters: Optional[dict] = None) -> None:
        self.filters = filters

    @classmethod
    def from_dict(cls, adict: Mapping):
        invalid_request = InvalidRequestObject()

        if "filters" in adict:
            if not isinstance(adict["filters"], Mapping):
                invalid_request.add_error("filters", "Is not iterable")
                return invalid_request

            for key, value in adict["filters"].items():
                if key not in cls.accepted_filters:
                    invalid_request.add_error(
                        "filters", f"{key} cannot be used as a filter"
                    )

        if invalid_request.has_errors():
            return invalid_request

        return cls(filters=adict.get("filters", None))
