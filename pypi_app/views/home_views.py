import flask

import pypi_app.services.package_service as package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
def index():
    trending_packages, new_packages = package_service.get_latest_packages()
    return flask.render_template('home/index.html',
                                 trending_packages=trending_packages, new_packages=new_packages)

@blueprint.route('/about/')
def about():
    return flask.render_template('home/about.html')