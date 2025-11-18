from flask import Flask
from flask_bcrypt import Bcrypt
from webapp.config import ProductionCfg, DevelopmentCfg
from db.DB import DB
from flask_login import LoginManager

"""Enable for Development mode"""
cfg = DevelopmentCfg
"""Enable for Production mode"""
# cfg = ProductionCfg

bcrypt = Bcrypt()

login_manger = LoginManager()
login_manger.login_view =  "auth_controller.user_login"
login_manger.login_message = cfg.LOGIN_MSG
login_manger.login_message_category = "warning"

def setup(app):
    print("setting things up")

    login_manger.init_app(app= app)

    DB.set_up(cfg.DB_URL)
    # setup SU
    hashed = bcrypt.generate_password_hash(cfg.SU_PASS).decode('utf-8')

    DB.add_user(cfg.SU_NAME,cfg.SU_EMAIL,hashed,True)


def create_app():
    app = Flask(__name__, template_folder=cfg.VIEWS_DIR, static_folder=cfg.STATIC_DIR)
    app.config.from_object(cfg)
    with app.app_context():
        bcrypt.init_app(app)

        setup(app)
        


        # cfg.init_app()
        
        from webapp.routes.MainRouter import MainRouter
        from webapp.routes.AuthRouter import AuthRouter
        # from webapp.routes.ArticleRoute import ArticleRoute
        
        app.register_blueprint(MainRouter)
        
        app.register_blueprint(AuthRouter)
        # app.register_blueprint(ArticleRoute)
        
    # الموجهات وصفحات الخطأ #

    return app




