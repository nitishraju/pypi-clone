import flask

import pypi_app.services.package_service as package_service

blueprint = flask.Blueprint('package', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
def package_name_details(package_name: str):
    return 'Package details for {}'.format(package_name)

@blueprint.route('/<int:package_rank>')
def package_rank_details(package_rank: int):
    return 'Details for the number {} most popular package.'.format(package_rank)