import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import pypi_app.views.home_views as home_views
import pypi_app.views.package_views as package_views
import pypi_app.views.account_views as account_views
import pypi_app.views.cms_views as cms_views

app = flask.Flask(__name__)

app.register_blueprint(home_views.blueprint)
app.register_blueprint(package_views.blueprint)
app.register_blueprint(account_views.blueprint)
app.register_blueprint(cms_views.blueprint)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
