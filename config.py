import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecret')
    DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_FOLDER', './downloads')
    GOOGLE_CREDENTIALS = os.getenv('GOOGLE_CREDENTIALS', 'config/credentials.json')
