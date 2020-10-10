import flask

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


#INDEX METHOD
@blueprint.route('/account')
def index():
    return flask.render_template('account/index.html')


#LOGIN METHODS
@blueprint.route('/account/login', methods=['GET'])
def login_get():
    return flask.render_template('account/login.html')

@blueprint.route('/account/login', methods=['POST'])
def login_post():
    return flask.render_template('account/login.html')


#REGISTER METHODS
@blueprint.route('/account/register', methods=['GET'])
def register_get():
    return flask.render_template('account/register.html')

@blueprint.route('/account/register', methods=['POST'])
def register_post():
    return flask.render_template('account/register.html')


#LOGOUT METHODS
@blueprint.route('/account/logout')
def logout():
    return flask.render_template('account/logout.html')