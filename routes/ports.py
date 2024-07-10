from flask import Flask, jsonify, request, make_response, Blueprint
from decorators.token_required import token_required
import json
from sqlalchemy import or_
import os

image_routes = Blueprint('devices_routes', __name__)
key=os.getenv('SECRET_JWT_KEY')

@devices_routes.route('', methods =['GET'])
@token_required(key, requires_admin=True)
def get_devices(current_user):
    devices = Dev.query.all()
    results = []
    for image in images:
        result = {
            'id': image.id,
            'format': image.format,
            'name': image.name,
            'file_path': image.file_path,
            'status': image.status.value,
        }
        results.append(result)
    return jsonify(results)
