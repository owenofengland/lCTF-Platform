from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .secure import db_uri, secret_key

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.User import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.errorhandler(404)
    def error_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("500.html"), 500

    from .util.chal_import import add_to_db

    from .routes.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes.scoreboard import scoreboard as scoreboard_blueprint
    app.register_blueprint(scoreboard_blueprint)

    from .routes.challenges import challenges as challenges_blueprint
    app.register_blueprint(challenges_blueprint)

    app.before_first_request(add_to_db)

    return app
