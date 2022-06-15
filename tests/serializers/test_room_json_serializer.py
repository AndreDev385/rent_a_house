import uuid
import json

from rent_a_house.domain import room as r
from rent_a_house.serializers import room_json_serializer as rjs


def test_serializer_room():
    code = uuid.uuid4()
    room = r.Room(code=code, size=200, price=10, longitude=-0.09, latitude=51.123)
    expected_json = f"""
    {{
        "code": "{code}",
        "size": 200,
        "price": 10,
        "longitude": -0.09,
        "latitude": 51.123
    }}
    """
    json_room = json.dumps(room, cls=rjs.RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
