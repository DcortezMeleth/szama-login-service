from flask import Blueprint, abort, jsonify, request

from config import mongo
from user.models import User

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<user_name>', methods=['GET'])
def get_user(user_name):
    dbuser = mongo.db.users.find({'name': user_name})
    if not dbuser:
        abort(404)

    return jsonify(dbuser)


@user.route('/', methods=['POST'])
def add_user():
    content = request.get_json()
    dbuser = User(**content)
    mongo.db.users.save(dbuser)
    return jsonify(status='OK')
