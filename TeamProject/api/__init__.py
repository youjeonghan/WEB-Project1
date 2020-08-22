from flask import Blueprint

api = Blueprint('api',__name__)
print(__name__)

from . import board