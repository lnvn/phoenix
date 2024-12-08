import os

class Config:
    SECRET_KEY = 'your_secret_key'  # Use a secret key for sessions
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Path to SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable unnecessary track modifications
    UPLOAD_FOLDER = 'static/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
