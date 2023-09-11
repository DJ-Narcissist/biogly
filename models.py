"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


DEFAULT_IMAGE_URL = 

class User(db.Model):
    """User model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(50), nullable = False, unique = True)
    last_name = db.Column(db.String(50), nullable = False, unique = False)
    image_url = db.Column(db.String(200), nullable = False, default = DEFAULT_IMAGE_URL)


@property
def full_name(self):
    """Return username"""
    return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connects database to Flask"""
    
    db.app = app
    db.init_app(app)
