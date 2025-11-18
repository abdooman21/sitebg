from flask_login import UserMixin
from webapp import login_manger
from db.DB import DB
from webapp.models.LikeModel import Like
from webapp.models.SubscribeModel import StripeCustomer

@login_manger.user_loader
def load_user(user_id):
    """
    Load user from database by ID.
    This is called by Flask-Login to reload the user object from the user ID in session.
    """
    return User.get_by_id(int(user_id))
 

class User(UserMixin):
    """User model with Flask-Login support"""
    
    def __init__(self, id, join_date, username, email, password, is_admin):
        self.id = id
        self.join_date = join_date
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = bool(is_admin)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    # Flask-Login required methods (inherited from UserMixin):
    # - get_id() - returns self.id as string
    # - is_authenticated - returns True if user is authenticated
    # - is_active - returns True (override if you have active/inactive users)
    # - is_anonymous - returns False
    
    def get_likes(self):
        """Get all likes made by this user"""
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM likes WHERE liked_user = ?", (self.id,))
        rows = cur.fetchall()
        conn.close()
        return [Like(*row) for row in rows]
    
    def get_stripe_customers(self):
        """Get all Stripe customer records for this user"""
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM stripe_customers WHERE user_id = ?", (self.id,))
        rows = cur.fetchall()
        conn.close()
        return [StripeCustomer(*row) for row in rows]
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID - used by user_loader"""
        user_data = DB.get_user(user_id)
        if user_data:
            # DB.get_user returns (id, join_date, username, email, password, is_admin)
            return User(*user_data)
        return None
    
    @staticmethod
    def get_by_email(email):
        """Get user by email - used for login"""
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, join_date, username, email, password, is_admin
            FROM users
            WHERE email = ?
        """, (email,))
        user_data = cur.fetchone()
        conn.close()
        
        if user_data:
            return User(*user_data)
        return None
    
    @staticmethod
    def get_by_username(username):
        """Get user by username"""
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, join_date, username, email, password, is_admin
            FROM users
            WHERE username = ?
        """, (username,))
        user_data = cur.fetchone()
        conn.close()
        
        if user_data:
            return User(*user_data)
        return None

# from db.DB import DB
# from webapp.models.LikeModel import Like
# from webapp.models.SubscribeModel import StripeCustomer
# from webapp import login_manger


# @login_manger.user_loader
# def load_user(user_id):
#     return DB.get_user(int(user_id))
 
# class User:
#     def __init__(self, id, join_date, username, email, password, is_admin):
#         self.id = id
#         self.join_date = join_date
#         self.username = username
#         self.email = email
#         self.password = password
#         self.is_admin = bool(is_admin)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"
    
#     def get_likes(self):
#         conn = DB.get_db()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM likes WHERE liked_user = ?", (self.id,))
#         rows = cur.fetchall()
#         conn.close()
#         return [Like(*row) for row in rows]

#     # Equivalent to: user.stripe_customers
#     def get_stripe_customers(self):
#         conn = DB.get_db()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM stripe_customers WHERE user_id = ?", (self.id,))
#         rows = cur.fetchall()
#         conn.close()
#         return [StripeCustomer(*row) for row in rows]