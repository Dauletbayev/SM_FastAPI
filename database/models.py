from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    phone_number = Column(String, unique=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    user_city = Column(String, nullable=True)
    birthday = Column(String, nullable=True)
    reg_day = Column(DateTime)

class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, autoincrement=True, primary_key=True)
    hashtag_name = Column(String, unique=True)
    hashtag_date = Column(DateTime)

class UserPost(Base):
    __tablename__ = 'user_posts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    main_text = Column(String, nullable=True)
    hashtag_name = Column(String, ForeignKey('hashtags.hashtag_name'), nullable=True)
    post_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    hashtag_fk = relationship(Hashtag, lazy='subquery')

class PostPhoto(Base):
    __tablename__ = 'post_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    photo_path = Column(String, nullable=False)
    post_date = Column(DateTime)

    post_fk = relationship(UserPost, lazy='subquery')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    comment_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')


