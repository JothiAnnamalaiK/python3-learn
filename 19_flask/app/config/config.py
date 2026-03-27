import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()  # loads .env file


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    USE_CUSTOM_ERROR_PAGES = True

    FLASK_RUN_HOST = "127.0.0.1"
    FLASK_RUN_PORT = 5000
    BASE_URL = "/"  # optional, can be used for reverse URL generation


class DevelopmentConfig(Config):
    DEBUG = True
    USE_CUSTOM_ERROR_PAGES = True
    DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
    DB_PORT = os.environ.get("MYSQL_PORT", "3306")
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD = quote_plus(
        os.environ.get("MYSQL_ROOT_PASSWORD", "")
    )  # quote_plus = to use special chars in password
    DB_NAME = os.environ.get("MYSQL_DATABASE", "py-flask-app")

    # for using SQL:# pip install pymysql flask_sqlalchemy

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"  # pip install pymysql

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    )

    FLASK_RUN_HOST = "0.0.0.0"  # listen on all interfaces (will connect in IP)
    FLASK_RUN_PORT = 3000
    BASE_URL = "/"


class ProductionConfig(Config):
    DEBUG = False
    USE_CUSTOM_ERROR_PAGES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    FLASK_RUN_HOST = "0.0.0.0"
    FLASK_RUN_PORT = 80
    BASE_URL = "/myapp"  # if your app is under subpath
