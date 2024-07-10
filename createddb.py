from app import app
from app import db
from persistence.models import User, UserRole, Device
import uuid
from werkzeug.security import generate_password_hash

with app.app_context():
    db.drop_all()    
    db.create_all()

    # Valores CRUD tables
    user =  User(
            public_id = str(uuid.uuid4()),
            name = "Admin",
            username = "admin",
            password = generate_password_hash("password"),
            role = UserRole.ADMIN
        )
    device = Device(
        idQR = "switch1",
        idLnms = "45",
        name = "SwitchPrueba",
        data = ""
    )

    db.session.add(user)
    db.session.add(device)
    db.session.commit()