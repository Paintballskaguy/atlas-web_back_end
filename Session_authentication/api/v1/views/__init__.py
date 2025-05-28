#!/usr/bin/env python3
""" Views Initialization """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.users import *

# Import and register session auth route after all other imports
from api.v1.views.session_auth import handle_login
app_views.add_url_rule(
    '/auth_session/login',
    view_func=handle_login,
    methods=['POST'],
    strict_slashes=False
)
