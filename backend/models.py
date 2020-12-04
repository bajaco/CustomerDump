from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    resolved_tickets = relationship('Ticket', back_populates='resolved_by')

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
    description = Column(String)
    solution = Column(String)
    resolved = Column(Boolean, default=False)
    data = Column(String)
    resolved_by_id = Column(Integer, ForeignKey('users.id'))
    resolved_by = relationship('User', back_populates='resolved_tickets')

