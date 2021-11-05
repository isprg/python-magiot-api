import os

from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# get .env settings
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOSTIP = os.environ.get("DB_HOSTIP")
DB_NAME = os.environ.get("DB_NAME")

DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOSTIP,
    DB_NAME,
)
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)
session.expire_on_commit = False

Base = declarative_base()
Base.query = session.query_property()
