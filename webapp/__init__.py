from flask import Flask
from flask_bcrypt import Bcrypt
from webapp.config import ProductionCfg, DevelopmentCfg

"""Enable for Development mode"""
cfg = DevelopmentCfg
"""Enable for Production mode"""
# cfg = ProductionCfg

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, template_folder=cfg.VIEWS_DIR, static_folder=cfg.STATIC_DIR)
    app.config.from_object(cfg)
    with app.app_context():
        bcrypt.init_app(app)
        
        from webapp.routes.MainRouter import MainRouter
        from webapp.routes.ArticleRoute import ArticleRoute
        cfg.init_app
        
        app.register_blueprint(MainRouter)
        app.register_blueprint(ArticleRoute)
    # الموجهات وصفحات الخطأ #
    return app