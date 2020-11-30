import sqlalchemy as sa
import datetime

from pypi_app.data.modelbase import ModelBase


class User(ModelBase):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = sa.Column(sa.String, nullable=True)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)