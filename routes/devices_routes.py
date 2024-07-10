from flask import Flask, jsonify, request, make_response, Blueprint
from sqlalchemy import or_
from persistence.models import Device
from services.devices_service import DeviceService
from decorators.token_required import token_required
import json
import traceback
import os

devices_routes = Blueprint('devices_routes',__name__)
key=os.getenv('SECRET_JWT_KEY')

# Ruta para obtener un dispositivo por idLnms
@devices_routes.route('/<int:idLnms>', methods=['GET'])
@token_required(key, requires_admin=True)
def get_device_by_id(idLnms):
    rec = Device.query.filter_by(idLnms=idLnms).first()
    
    if rec is None:
        return jsonify({'error': 'Device not found'}), 404
    
    try:
        deviceData = DeviceService.get_device_info(idLnms)
    except Exception as e:
        traceback.print_exc()
        deviceData = None

    if deviceData:
        # Convertir rec.data a cadena JSON si es necesario
        rec.data = json.dumps(deviceData)
        
        return jsonify(deviceData)
    else:
        if rec.data:
            # Si rec.data es una cadena JSON, devolverla como tal
            if isinstance(rec.data, str):
                return jsonify(json.loads(rec.data))
            return jsonify(rec.data)
        return jsonify({"error": "Device not found via API"}), 404
