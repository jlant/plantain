import datetime

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase("plantain.db")


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    wsc = CharField()

    class Meta:
        database = DATABASE
        order_by = ("-joined_at",)  # descending order
    
    def get_qa_data(self):
        """Get the most recent data from the QA table""" 
        return QA.select().where(QA.user == self).order_by(QA.timestamp.desc()).get()

    @classmethod
    def create_user(cls, email, password, wsc):
        try:
            with DATABASE.transaction():
                cls.create(
                    username = email.split("@")[0],  # name in users email
                    email = email,
                    password = generate_password_hash(password),
                    wsc = wsc)
        except IntegrityError:
            raise ValueError("User already exists.")


class QA(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(model=User, backref="qa_content")
    responsibilities = TextField()
    safety = TextField()
    stream_install = TextField()
    station_desc = TextField()
    station_photos = TextField()

    class Meta:
        database = DATABASE
        order_by = ("-timestamp",)  # descending order


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, QA], safe=True)
    DATABASE.close()

