from flask import Blueprint
from webapp.controller.auth.UserController import UserController


AuthRouter = Blueprint("auth_controller",__name__)


AuthRouter.route("/register", methods=["GET","POST"])(UserController.user_sginup)
AuthRouter.route("/login", methods=["GET","POST"])(UserController.user_login)
AuthRouter.route("/logout")(UserController.user_logout)
