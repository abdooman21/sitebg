from db.DB import DB
from webapp.models.LikeModel import Like
from webapp.models.SubscribeModel import StripeCustomer

 
class User:
    def __init__(self, id, join_date, username, email, password, is_admin):
        self.id = id
        self.join_date = join_date
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = bool(is_admin)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    def get_likes(self):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM likes WHERE liked_user = ?", (self.id,))
        rows = cur.fetchall()
        conn.close()
        return [Like(*row) for row in rows]

    # Equivalent to: user.stripe_customers
    def get_stripe_customers(self):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM stripe_customers WHERE user_id = ?", (self.id,))
        rows = cur.fetchall()
        conn.close()
        return [StripeCustomer(*row) for row in rows]