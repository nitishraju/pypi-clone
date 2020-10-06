import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import pypi_app.views.home_views as home_views

app = flask.Flask(__name__)

app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
