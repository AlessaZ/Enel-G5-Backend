from flask import Flask, jsonify, request, make_response, Blueprint
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from persistence.models import User, UserRole, db
from decorators.token_required import token_required
import jwt
from datetime import datetime, timedelta
import uuid
import os
import json

auth_routes = Blueprint('auth_routes', __name__)
key=os.getenv('SECRET_JWT_KEY')

# route for logging user in
@auth_routes.route('/login', methods =['POST'])
@token_required(key, requires_admin=True)
def login():
    # creates dictionary of form data
    data = json.loads(request.data)
    username, password = data.get('username'), data.get('password')
  
    if not data or not username or not password:
        return make_response(
            400,{'message' : 'Username and password are required'}
        )
  
    user = User.query\
        .filter_by(username = username)\
        .first()
  
    if not user:
        return make_response(
            400, {'message' : 'User does not exist'}
        )
  
    if check_password_hash(user.password, password):
        # Genera el JWT Token
        token = jwt.encode({
            'public_id': user.public_id,
            'iss_time': str(datetime.utcnow()),
            'exp' : datetime.utcnow() + timedelta(minutes = 720)
        }, key, algorithm='HS256')
  
        return make_response({'token' : token, 'name': user.name, 'role': user.role.value}, 200)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'message' : 'Wrong password'}
    )