from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, Integer, String, Float, DateTime, TIMESTAMP

from .config import Base


class Device(Base):
    __tablename__ = 'devices'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128),
                  nullable=False, unique=True)
    status = Column('status', Integer, server_default="0")
    created_at = Column('created_at', TIMESTAMP,
                        server_default=current_timestamp())
    updated_at = Column('updated_at', TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at':  self.created_at,
            'updated_at': self.updated_at
        }
