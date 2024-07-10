from flask import request, jsonify
from functools import wraps
from persistence.models import User, UserRole
import jwt

def token_required(key, requires_admin = False):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            # jwt is passed in the request header
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            # return 401 if token is not passed
            if not token:
                return jsonify({'message' : 'No token was given'}), 401
            
            try:
                data = jwt.decode(token, key, algorithms=['HS256'])
                if requires_admin:
                    current_user = User.query\
                        .filter_by(public_id = data['public_id'])\
                        .filter_by(role = UserRole.ADMIN)\
                        .first() 
                else:
                    current_user = User.query\
                        .filter_by(public_id = data['public_id'])\
                        .first()    
                
                if not current_user:
                    return jsonify({
                        'message' : 'You are not authorized for this endpoint'
                    }), 401
            except:
                return jsonify({
                    'message' : 'You are not authorized for this endpoint'
                }), 401
            # returns the current logged in users context to the routes
            return  f(current_user, *args, **kwargs)
    
        return decorated
    return decorator