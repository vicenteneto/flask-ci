from flask import Blueprint, request

blueprint = Blueprint('users', __name__, url_prefix='/users')


@blueprint.route('', methods=['POST', 'GET'])
def create_list():
    if request.method == 'POST':
        return 'Create user'
    return 'List users'


@blueprint.route('/<user_id>', methods=['GET', 'DELETE', 'PUT'])
def read_delete_update(user_id):
    if request.method == 'GET':
        return 'Read user %s' % user_id
    elif request.method == 'DELETE':
        return 'Delete user %s' % user_id
    return 'Update user %s' % user_id
