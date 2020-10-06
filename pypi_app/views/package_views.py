import flask

import pypi_app.services.package_service as package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
def index():
    test_packages = package_service.get_latest_packages()
    return flask.render_template('home/index.html', packages=test_packages)