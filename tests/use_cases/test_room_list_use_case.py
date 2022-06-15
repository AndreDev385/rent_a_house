from time import monotonic
import pytest
import uuid

from unittest import mock


from rent_a_house.domain import room as r
from rent_a_house.use_cases import room_list_use_case as uc


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
    result = room_list_use_case.execute()

    repo.list.assert_called_with()
    assert result == domain_rooms
