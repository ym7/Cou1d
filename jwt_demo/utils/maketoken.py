import jwt
import datetime
from jwt import exceptions
from django.conf import settings


salt = settings.SECRET_KEY

def create_token(payload):
    headers = {
        'typ':'jwt',
        'alg':'HS256'
    }
    # 构造payload
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=1) # 超时时间

    token = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers).decode('utf-8')
    return token

def parse_payload(token):
    res = {'status':False,'data':None,'error':None}
    try:
        ver_payload = jwt.decode(token,salt,True)
        res['status']=True
        res['data'] = ver_payload
    except exceptions.ExpiredSignatureError:
        res['error'] = 'token失效'
    except jwt.DecodeError:
        res['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        res['error'] = '非法token'
    return res
