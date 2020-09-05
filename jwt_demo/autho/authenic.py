from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from utils.maketoken import parse_payload

class AuthThrough(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        payload =parse_payload(token)
        if not payload['status']:
            raise exceptions.AuthenticationFailed(payload)
        return (payload,token)
