import sqlite3

class DB(): 
    dbUrl = None
    @classmethod
    def set_up(cls, url):
        cls.dbUrl = url    # update static variable

    @classmethod
    def get_db(cls):
        if cls.dbUrl is None:
            raise ValueError("DB not configured. Call DB.set_up(url) first.")
        return sqlite3.connect(cls.dbUrl)
    
    def create_tables():
        conn = DB.get_db()
        cur = conn.cursor()

        # Enable foreign keys (important!)
        cur.execute("PRAGMA foreign_keys = ON;")

        # USERS TABLE
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            join_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT 0
        );
        """)

        # ARTICLES TABLE
        cur.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            article_img TEXT NOT NULL DEFAULT 'default.png',
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE SET NULL
        );
        """)

        # LIKES TABLE (CASCADE on delete)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS likes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            liked_user INTEGER NOT NULL,
            article_id INTEGER NOT NULL,
            FOREIGN KEY(liked_user) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY(article_id) REFERENCES articles(id) ON DELETE CASCADE
        );
        """)

        # STRIPE CUSTOMER TABLE
        cur.execute("""
        CREATE TABLE IF NOT EXISTS stripe_customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscription_type TEXT,
            status TEXT,
            customer_id TEXT,
            subscription_id TEXT,
            amount INTEGER,
            subscription_start DATETIME,
            subscription_end DATETIME,
            subscription_canceled BOOLEAN,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        """)

        conn.commit()
        conn.close()

    def add_user(username, email, password, is_admin=False):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (username, email, password, is_admin)
            VALUES (?, ?, ?, ?)
        """, (username, email, password, is_admin))
        conn.commit()
        conn.close()
        
    def add_article(title, content, user_id, article_img="default.png"):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO articles (title, content, article_img, user_id)
            VALUES (?, ?, ?, ?)
        """, (title, content, article_img, user_id))
        conn.commit()
        conn.close()

    def like_article(user_id, article_id):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO likes (liked_user, article_id)
            VALUES (?, ?)
        """, (user_id, article_id))
        conn.commit()
        conn.close()

    def add_stripe_customer(user_id, subscription_type, status):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO stripe_customers (user_id, subscription_type, status)
            VALUES (?, ?, ?)
        """, (user_id, subscription_type, status))
        conn.commit()
        conn.close()
