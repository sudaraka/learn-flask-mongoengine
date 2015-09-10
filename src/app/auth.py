""" Authentication subroutines """

from functools import wraps
from flask import request, Response


def check_auth(username, password):
    """ Check if given username/password are valid """

    return username == 'admin' and password == 'test'


def authenticate():
    """ Send HTTP basic auth request """

    return Response(
        'Need authentication to access this URL\n'
        'Please enter your login credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    """ Authentication decorator for views """

    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)

    return decorated
