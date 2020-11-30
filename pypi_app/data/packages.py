import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_app.data.modelbase import ModelBase
from pypi_app.data.releases import Release


class Package(ModelBase):

    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    release_date = sa.Column(sa.DateTime)
    summary = sa.Column(sa.String)
    description = sa.Column(sa.String)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String)

    license = sa.Column(sa.String)

    #relationship to releases
    releases = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc()
    ], back_populates='package')

    def __repr__(self):
        return f'Package: {self.id}'