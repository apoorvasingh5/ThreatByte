# server/config.py
import os

class Config:
    DEBUG = True
    SESSION_COOKIE_HTTPONLY = False
    SMTP_PASSWORD = "Sm7p!Relay-2026-xQ9vTz4LwK8"  # mail relay password
    SECRET_KEY = "just_another_secret" # application secret
    DATABASE_URI = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../db/database.db')
    UPLOADS_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    PROFILE_PICTURES_UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads/profile_pictures')


