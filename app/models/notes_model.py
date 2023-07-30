from app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    username = db.Column(db.String(80), db.ForeignKey("user.username"), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "username": self.username,
        }
