import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    profile_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    
    following_user_id = Column(Integer, ForeignKey('following.user.id'))
    user = relationship(User)

    followed_user_id = Column(Integer, ForeignKey('followed.user.id'))
    user = relationship(User)

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    date= Column (Date, nullable= False)


class media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(post)

    url= Column (String(500), nullable= False)
    type = Column (String(250), nullable= False)

class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(post)


    comment_text= Column (String(1000), nullable= True)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
