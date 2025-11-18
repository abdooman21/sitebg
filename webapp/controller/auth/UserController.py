# blog > controllers > auth > UserController.py

from flask import render_template, url_for, flash, redirect, request
from webapp.models.AuthModel import User
from webapp.forms.AuthForm import LoginForm, RegisterForm
from webapp import bcrypt, DB

from flask_login import login_user, current_user, login_required, logout_user

class UserController:
    def user_login():
        # If the user is already authenticated, redirect them away from the login page
        if current_user.is_authenticated:
            return redirect(url_for('main_controller.home'))

        form = LoginForm()

        if form.validate_on_submit():
            user = None # Initialize user to None

            # Check if email was provided and is valid
            if form.email.data:
                user = User.get_by_email(email=form.email.data)
            # If email was not provided OR no user was found by email,
            # then check if username was provided and try to find by username
            if user is None and form.username.data:
                user = User.get_by_username(username=form.username.data)

            # Now, check if a user was found and if the password is correct
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data if hasattr(form, 'remember') else False) # Assuming remember field might exist
                flash("تم تسجيل الدخول بنجاح", "success") # Login successful message
                # Redirect to the 'next' page if it exists in the request arguments, otherwise to home
                next_page = request.args.get('next')
                return redirect(next_page or url_for('main_controller.home'))
            else:
                flash("فشل تسجيل الدخول! تأكد من كتابة البريد الإلكتروني أو اسم المستخدم وكلمة السر بشكل صحيح", "danger")
                return redirect(url_for('auth_controller.user_login'))

        # If it's a GET request or form validation failed (but it's not due to
        # the custom "either or" check, which would have already added errors),
        # render the login page.
        return render_template('auth/login.jinja', form=form, title="تسجيل الدخول")
    
    def user_sginup():
        if current_user.is_authenticated:
            return redirect(url_for('main_controller.home'))

        form = RegisterForm()
        if form.validate_on_submit():
            hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            usname = form.username
            DB.add_user(usname,form.email,hashed,False)
            login_user(user=User.get_by_username(username=usname))
            flash(f'welcome {usname} you can read forms now', "success")
            return redirect(url_for('main_controller.home'))
        return render_template("auth/register.jinja",form=form, title="signup")
    
    @login_required
    def user_logout():
        logout_user()
        flash(f'bye logging you out', "success")
        return redirect(url_for('main_controller.home'))