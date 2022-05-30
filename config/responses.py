from rest_framework.response import Response
from rest_framework import status


class ResponseFail(Response):
    def __init__(self, data="", status=200):
        data = {"status": "fail", "data": data}
        super().__init__(data, status=status)


class ResponseSuccess(Response):
    def __init__(self, data="", headers=None):
        if isinstance(data, Response):
            data = data.data
        
        data = {"status": "success", "data": data}
        if headers:
            data["headers"] = headers
        super().__init__(data, status=status.HTTP_200_OK)