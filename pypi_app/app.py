import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

#To be removed later; Added due to issues with WSL2
DB_DIR = os.getenv('DB_DIR')

app = flask.Flask(__name__)

def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)

def register_blueprints():
    from pypi_app.views import home_views
    from pypi_app.views import account_views
    from pypi_app.views import package_views
    from pypi_app.views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(cms_views.blueprint)

def setup_db():
    import pypi_app.data.db_session as db_sess
    db_sess.global_init(DB_DIR)


if __name__ == '__main__':
    main()
