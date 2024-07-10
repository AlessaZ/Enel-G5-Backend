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
    
    user1 =  User(
            public_id = str(uuid.uuid4()),
            name = "Angel",
            username = "angelb",
            password = generate_password_hash("password"),
            role = UserRole.ADMIN
        )
    
    user2 =  User(
            public_id = str(uuid.uuid4()),
            name = "Enel-G5",
            username = "enelg5",
            password = generate_password_hash("password"),
            role = UserRole.ADMIN
        )

    device = Device(
        idLnms = "1",
        data = ""
    )

    device1 = Device(
        idLnms = "2",
        data = ""
    )

    device2 = Device(
        idLnms = "3",
        data = ""
    )

    db.session.add(user)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(device)
    db.session.add(device1)
    db.session.add(device2)
    db.session.commit()