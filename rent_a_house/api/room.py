import json

from flask import Blueprint, request
from flask.wrappers import Response

from rent_a_house.repositories import mongorepo as mr
from rent_a_house.use_cases import room_list_use_case as uc
from rent_a_house.serializers import room_json_serializer as ser
from rent_a_house.request_objects import room_list_request_objects as req
from rent_a_house.response_objects import response_object as res


blueprint = Blueprint("room", __name__)
"""room1 = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "size": 215,
    "price": 39,
    "longitude": -0.09998975,
    "latitude": 51.75436293,
}
room2 = {
    "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
    "size": 405,
    "price": 66,
    "longitude": 0.18228006,
    "latitude": 51.74640997,
}
room3 = {
    "code": "913694c6-435a-4366-ba0d-da5334a611b2",
    "size": 56,
    "price": 60,
    "longitude": 0.27891577,
    "latitude": 51.45994069,
}"""


connection_data = {
    "dbname": "rentomaticdb",
    "user": "root",
    "password": "rentomaticdb",
    "host": "localhost",
}

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
    res.ResponseFailure.RESOURCE_ERROR: 404,
}


@blueprint.route("/rooms", methods=["GET"])
def room():
    qrystr_params = {
        "filters": {},
    }
    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values
    request_object = req.RoomListRequestObject.from_dict(qrystr_params)
    repo = mr.MongoRepo(connection_data)
    use_case = uc.RoomListUseCase(repo)
    response = use_case.execute(request_object)
    return Response(
        json.dumps(response.value, cls=ser.RoomJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )
