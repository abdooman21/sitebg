from flask import render_template, url_for, flash, redirect, request
from webapp.models.AuthModel import User
from webapp.forms.AuthForm import LoginForm, RegisterForm
from webapp import bcrypt
from db.DB import DB
from flask_login import login_user, current_user, login_required, logout_user

class UserController:
    
    @staticmethod
    def user_login():
        """Handle user login"""
        # If the user is already authenticated, redirect them away from the login page
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        
        form = LoginForm()
        
        if form.validate_on_submit():
            user = None  # Initialize user to None
            
            # Check if email was provided and is valid
            if form.email.data:
                user = User.get_by_email(email=form.email.data)
            
            # If email was not provided OR no user was found by email,
            # then check if username was provided and try to find by username
            if user is None and hasattr(form, 'username') and form.username.data:
                user = User.get_by_username(username=form.username.data)
            
            # Now, check if a user was found and if the password is correct
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                remember_me = form.remember.data if hasattr(form, 'remember') else False
                login_user(user, remember=remember_me)
                flash("تم تسجيل الدخول بنجاح", "success")
                
                # Redirect to the 'next' page if it exists, otherwise to home
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
            else:
                flash("فشل تسجيل الدخول! تأكد من كتابة البريد الإلكتروني أو اسم المستخدم وكلمة السر بشكل صحيح", "danger")
                return redirect(url_for('auth.user_login'))
        
        # If it's a GET request or form validation failed, render the login page
        return render_template('auth/login.jinja', form=form, title="تسجيل الدخول")
    
    @staticmethod
    def user_register():
        """Handle user registration"""
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        
        form = RegisterForm()
        
        if form.validate_on_submit():
            # Hash the password
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            
            # Get username from form data (FIXED: was missing .data)
            username = form.username.data
            email = form.email.data
            
            # Add user to database
            user_id = DB.add_user(username, email, hashed_password, False)
            
            # Log the user in automatically after registration
            user = User.get_by_username(username=username)
            if user:
                login_user(user)
                flash(f'مرحباً {username}! تم إنشاء حسابك بنجاح', "success")
                return redirect(url_for('main.home'))
            else:
                flash('حدث خطأ أثناء تسجيل الدخول. يرجى المحاولة مرة أخرى', "danger")
                return redirect(url_for('auth.user_login'))
        
        return render_template("auth/register.jinja", form=form, title="إنشاء حساب")
    
    @staticmethod
    @login_required
    def user_logout():
        """Handle user logout"""
        username = current_user.username
        logout_user()
        flash(f'إلى اللقاء {username}! تم تسجيل الخروج بنجاح', "success")
        return redirect(url_for('main.home'))