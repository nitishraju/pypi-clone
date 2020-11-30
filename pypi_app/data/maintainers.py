import sqlalchemy as sa
from pypi_app.data.modelbase import ModelBase


class Maintainer(ModelBase):

    __tablename__ = 'maintainers'

    user_id = sa.Column(sa.Integer, primary_key=True)
    package_id = sa.Column(sa.String, primary_key=True)