import os
from pathlib import Path
from dotenv import load_dotenv
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

class ProductionCfg(Config):
    pass