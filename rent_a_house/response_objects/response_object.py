from ctypes import Union
from sre_constants import SUCCESS
from typing import Optional

from rent_a_house.request_objects.room_list_request_objects import (
    InvalidRequestObject,
)


class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None) -> None:
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self) -> bool:
        return True


class ResponseFailure:
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    PARAMETERS_ERROR = "ParametersError"

    def __init__(self, type_, message) -> None:
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg) -> str:
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__}: {msg}"
        return msg

    @property
    def value(self) -> dict:
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_from_invalid_request_object(
        cls, invalid_request_object: InvalidRequestObject
    ):
        message = "\n".join(
            [
                "{}: {}".format(err["parameter"], err["message"])
                for err in invalid_request_object.errors
            ]
        )
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)
