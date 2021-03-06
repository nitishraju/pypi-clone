import sqlalchemy as sa
import datetime

from pypi_app.data.modelbase import ModelBase


class Language(ModelBase):

    __tablename__ = 'languages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    description = sa.Column(sa.String)