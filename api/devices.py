from flask import Blueprint, request, abort, jsonify

from .models.config import session
from .models.devices import Device

devices = Blueprint('devices', __name__, url_prefix='/api/v1/devices')


@devices.route('/', methods=['GET'])
def list_device():
    devices = session.query(Device).all()
    return jsonify({'devices': [device.to_dict() for device in devices]})


@devices.route('/<int:device_id>', methods=['GET'])
def get_device(device_id=None):
    device = session.query(Device).filter(Device.id == device_id).first()

    if not device:
        abort(404, {'code': 404, 'message': 'device not found'})

    return jsonify(device.to_dict())


@devices.route('/', methods=['POST'])
def post_device():
    payload = request.json
    name = payload.get('name')

    device = Device(name)
    session.add(device)

    try:
        session.commit()

        response = jsonify(device.to_dict())
        response.headers['Location'] = '/api/v1/devices/%d' % device.id
        return response, 201

    except Exception:
        session.rollback()
        abort(400, {'code': 400, 'message': 'value is already registered'})


@devices.route('/<int:device_id>', methods=['PUT'])
def put_device(device_id):
    device = session.query(Device).filter(Device.id == device_id).first()

    if not device:
        abort(404, {'code': 404, 'message': 'device not found'})

    payload = request.json
    device.status = payload.get('status')
    session.commit()

    return jsonify(device.to_dict())


@devices.route('/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    device = session.query(Device).filter(Device.id == device_id).first()

    if not device:
        abort(404, {'code': 404, 'message': 'device not found'})

    session.delete(device)
    session.commit()

    return jsonify(None), 204


@devices.errorhandler(400)
@devices.errorhandler(403)
@devices.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
