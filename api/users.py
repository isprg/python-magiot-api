from flask import Blueprint, request, abort, jsonify

from .models.config import session
from .models.users import User

users = Blueprint('users', __name__, url_prefix='/api/v1/users')


@users.route('/', methods=['GET'])
def list_user():
    users = session.query(User).all()
    return jsonify({'users': [user.to_dict() for user in users]})


@users.route('/<int:user_id>', methods=['GET'])
def get_user(user_id=None):
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        abort(404, {'code': 404, 'message': 'user not found'})

    return jsonify(user.to_dict())


@users.route('/', methods=['POST'])
def post_user():
    payload = request.json
    name = payload.get('name')

    user = User(name)
    session.add(user)

    try:
        session.commit()

        response = jsonify(user.to_dict())
        response.headers['Location'] = '/api/v1/users/%d' % user.id
        return response, 201

    except Exception:
        session.rollback()
        abort(400, {'code': 400, 'message': 'value is already registered'})


@users.route('/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        abort(404, {'code': 404, 'message': 'user not found'})

    payload = request.json
    user.rfid = payload.get('rfid')
    session.commit()

    return jsonify(user.to_dict())


@users.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        abort(404, {'code': 404, 'message': 'user not found'})

    session.delete(user)
    session.commit()

    return jsonify(None), 204
