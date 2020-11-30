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
    print(f'Connecting to DB through {connection_str}')

    engine = sa.create_engine(connection_str, echo=True, connect_args={"check_same_thread": False})
    factory = orm.sessionmaker(bind=engine)

    #noinspection PyUnresolvedReferences
    import pypi_app.data.__model_preloads

    ModelBase.metadata.create_all(engine)