import jwt
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication


def authenticateToken(view_func: object) -> object:
    def wrapper_func(request, *args, **kwargs):
        jwt_object = JWTTokenUserAuthentication()
        header = jwt_object.get_header(request)
        if header is None:
            res = Response({
                'code': 401,
                'error': True,
                'description': 'User Not Authenticated',
                'payload': None
            })
            res.status_code = 401
            return res
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def isStaff(view_func: object) -> object:
    def wrapper_func(request, *args, **kwargs):
        jwt_object = JWTTokenUserAuthentication()
        header = jwt_object.get_header(request)
        if header is None:
            res = Response({
                'code': 401,
                'error': True,
                'description': 'User Not Authenticated',
                'payload': None
            })
            res.status_code = 401
            return res
        else:
            raw_token = jwt_object.get_raw_token(header)
            jwtDecode = jwt.decode(jwt=raw_token, key='8e6cc7546ba343bcdf675dcdab3f33b9', algorithms=['HS256'])
            if jwtDecode['isStaff']:
                return view_func(request, *args, **kwargs)
            else:
                res = Response({
                    'code': 401,
                    'error': True,
                    'description': 'You do not have permission to perform this action',
                    'payload': None
                })
                res.status_code = 401
                return res
    return wrapper_func


def isAdmin(view_func: object) -> object:
    def wrapper_func(request, *args, **kwargs):
        jwt_object = JWTTokenUserAuthentication()
        header = jwt_object.get_header(request)
        if header is None:
            res = Response({
                'code': 401,
                'error': True,
                'description': 'User Not Authenticated',
                'payload': None
            })
            res.status_code = 401
            return res
        else:
            raw_token = jwt_object.get_raw_token(header)
            jwtDecode = jwt.decode(jwt=raw_token, key='8e6cc7546ba343bcdf675dcdab3f33b9', algorithms=['HS256'])
            if jwtDecode['isAdmin'] and jwtDecode['isStaff']:
                return view_func(request, *args, **kwargs)
            else:
                res = Response({
                    'code': 401,
                    'error': True,
                    'description': 'You do not have permission to perform this action (Admin Privilege required)',
                    'payload': None
                })
                res.status_code = 401
                return res
    return wrapper_func
