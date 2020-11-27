import sqlalchemy as sa


class Package:

    __tablename__ = 'packages'

    id = sa.column(sa.String, primary_key=True)
    release_date = sa.Column(sa.DateTime)
    summary = sa.Column(sa.String)
    description = sa.Column(sa.String)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String)

    license = sa.Column(sa.String)

    #TODO: Maintainers
    #TODO: RELEASES

    def __repr__(self):
        return f'Package: {self.id}'