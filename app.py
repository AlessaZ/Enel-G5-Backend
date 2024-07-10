from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth_routes import auth_routes
from routes.recurso_routes import recurso_routes
from dotenv import load_dotenv
from persistence.models import db
import os

load_dotenv()

app = Flask(__name__)
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/enelbd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(recurso_routes,url_prefix='/recurso')

db.init_app(app)