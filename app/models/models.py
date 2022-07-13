"""
Models for Scribble
"""

from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey, Boolean
from ..models.database import Base
from sqlalchemy.orm import relationship


class Player(Base):
    __tablename__ = "Player"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    playename = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    score = Column(Integer, nullable=False, server_default='0')


class Game(Base):
    __tablename__ = "Game"
    gameId = Column(String, nullable=False, primary_key=True)
    memberCount = Column(Integer)
    winner = Column(String)
    completed = Column(Boolean, nullable=False, server_default="False")
    created_by = Column(Integer, ForeignKey("Player.id", ondelete="CASCADE"), nullable=False)
    player = relationship("Player")
