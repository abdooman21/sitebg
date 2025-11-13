from flask import render_template 



class MainController:
    @staticmethod
    def home():
        """Render the home page"""
        data = {
            'title': 'الصفحة الرئيسية',  # Arabic for "Home Page"
            'page': 'home'
        }
        return render_template('main/home.jinja', **data)
    
    @staticmethod
    def about():
        """"About page"""
        data = {
            'title': 'من نحن',  # Arabic for "About Us"
            'page': 'about'
        }
        return render_template('main/about.jinja',**data)
    
    @staticmethod   
    def contact():
        """Render the contact page"""
        data = {
            'title': 'اتصل بنا',  # Arabic for "Contact Us"
            'page': 'contact'
        }
        return render_template('main/contact.jinja', **data)