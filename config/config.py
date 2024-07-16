import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Uncomment the database configuration you prefer to use

    # SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'

    # MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'

    # PostgreSQL
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'

    # MongoDB
    # MONGODB_SETTINGS = {
    #     'db': 'myDatabase',
    #     'host': 'localhost',
    #     'port': 27017
    # }

    SQLALCHEMY_TRACK_MODIFICATIONS = False