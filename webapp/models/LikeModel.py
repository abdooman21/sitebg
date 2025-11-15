class Like:
    def __init__(self, id, created_date, liked_user, article_id):
        self.id = id
        self.created_date = created_date
        self.liked_user = liked_user
        self.article_id = article_id

    def __repr__(self):
        return f"Like(User {self.liked_user}, Article {self.article_id})"
