from flask import Blueprint
from webapp.controller.MainController import MainController

MainRouter = Blueprint("main", __name__)



MainRouter.route("/")(MainController.home)
MainRouter.route('/home')(MainController.home)

MainRouter.route('/about')(MainController.about)

MainRouter.route('/contact')(MainController.contact)


# from flask import Blueprint
# from webapp.controller.MainController import MainController

# MainRouter = Blueprint("main_controller", __name__)
# main_controller = MainController()


# # Define routes
# @MainRouter.route('/')
# @MainRouter.route('/home')
# def home():
#     return main_controller.home()

# @MainRouter.route('/about')
# def about():
#     return main_controller.about()

# @MainRouter.route('/contact')
# def contact():
#     return main_controller.contact()