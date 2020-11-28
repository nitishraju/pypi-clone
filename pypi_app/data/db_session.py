import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_app.data.modelbase import ModelBase

factory = None

def global_init(db_file: str):
    global factory

    if factory:
        return

    if not db_file.strip():
        raise FileNotFoundError('Please specify a valid database file.')

    connection_str = 'sqlite:///' + db_file.strip()

    engine = sa.create_engine(connection_str, echo=True)
    factory = orm.sessionmaker(bind=engine)

    #import allows sqlalchemy to create db using Package metadata
    from pypi_app.data.package import Package

    ModelBase.metadata.create_all(engine)