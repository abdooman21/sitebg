from db.DB import DB
from webapp.models.LikeModel import Like

class Article:
    def __init__(self, id, title, content, created_date, article_img, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.created_date = created_date
        self.article_img = article_img
        self.user_id = user_id

    def __repr__(self):
        return f"Article('{self.user_id}', '{self.title}')"
    
    def get_likes(self):
        conn = DB.get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM likes WHERE article_id = ?", (self.id,))
        rows = cur.fetchall()
        conn.close()
        return [Like(*row) for row in rows]