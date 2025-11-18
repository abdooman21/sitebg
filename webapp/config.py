import os
from pathlib import Path
from dotenv import load_dotenv
from db.DB import DB
load_dotenv()

class Config:
    TESTING = False
    DEBUG = False

class DevelopmentCfg(Config):
    DEBUG = True
    APP_DIR = Path(os.path.dirname(os.path.realpath(__file__)))  # Convert to Path object here
    VIEWS_DIR = APP_DIR / 'templates'
    CONTROLLERS_DIR = APP_DIR / "controller"
    STATIC_DIR = APP_DIR / "static"
    IMAGES_DIR = STATIC_DIR / "images"
    # vars
    DB_URL = os.environ.get("DB_URL")
    SU_NAME = os.environ.get("SU_NAME")
    SU_EMAIL = os.environ.get("SU_EMAIL")
    SU_PASS = os.environ.get("SU_PASS")
    LOGIN_MSG =  "You should be logged in first"
    
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_very_secret_and_random_dev_key_that_is_long_and_complex_12345"
    
class ProductionCfg(Config):
    pass