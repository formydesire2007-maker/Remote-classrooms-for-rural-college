from datetime import datetime

from models import db



class User(db.Model):

    __tablename__ = "users"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )


    password = db.Column(
        db.String(255),
        nullable=False
    )


    college = db.Column(
        db.String(150)
    )


    role = db.Column(
        db.String(50),
        default="student"
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



    def __init__(
        self,
        name,
        email,
        password,
        college=None,
        role="student"
    ):

        self.name = name
        self.email = email
        self.password = password
        self.college = college
        self.role = role



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "email": self.email,

            "college": self.college,

            "role": self.role,

            "created_at":
                self.created_at.isoformat()

        }