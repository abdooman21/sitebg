from flask import Blueprint
from site.controller.MainController import MainController

MainRouter = Blueprint("main_controller", __name__)

MainRouter.route("/")(MainController.home)