from flask import Flask, jsonify, request, make_response, Blueprint
from sqlalchemy import or_
from persistence.models import Device

recurso_routes = Blueprint('recurso_routes',__name__)

@recurso_routes.route('', methods=['GET'])
def get_device():
   # Obtiene todos los registros de device
    recurso_list = Device.query.all()
    results = []
    for rec in recurso_list:
        result = {
            'idQR' : rec.idQR,
            'idLnms' : rec.idLnms,
            'name' : rec.name,
            'updated_on' : rec.updated_on,
            'data' : rec.data
        }
        results.append(result)
    return jsonify(results)


