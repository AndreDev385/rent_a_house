import pytest
import uuid

from unittest import mock

from requests import request


from rent_a_house.domain import room as r
from rent_a_house.use_cases import room_list_use_case as uc
from rent_a_house.request_objects import room_list_request_objects as req
from rent_a_house.response_objects import response_object as res


@pytest.fixture
def domain_rooms():
    room_1 = r.Room(
        code=uuid.uuid4(),
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    room_2 = r.Room(
        code=uuid.uuid4(),
        size=300,
        price=20,
        longitude=89.75436293,
        latitude=123.12312,
    )

    room_3 = r.Room(
        code=uuid.uuid4(),
        size=93,
        price=48,
        longitude=0.33894476,
        latitude=51.39916678,
    )

    return [room_1, room_2, room_3]


def test_room_list_without_params(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    room_list_use_case = uc.RoomListUseCase(repo)
    request = req.RoomListRequestObject()

    response = room_list_use_case.execute(request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_rooms


def test_room_list_with_filters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = uc.RoomListUseCase(repo)
    qry_filters = {"code__eq": 5}
    request_object = req.RoomListRequestObject.from_dict({"filters": qry_filters})
    response_object = room_list_use_case.execute(request_object)
    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_rooms


def test_room_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")
    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({})
    response_object = room_list_use_case.execute(request_object)
    assert bool(response_object) is False
    assert response_object.value == {
        "type": res.ResponseFailure.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_room_list_handle_bad_request():
    repo = mock.Mock()
    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({"filters": 5})
    response_object = room_list_use_case.execute(request_object)
    assert bool(response_object) is False
    assert response_object.value == {
        "type": res.ResponseFailure.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }
