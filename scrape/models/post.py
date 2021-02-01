from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# we need this to create database models
Base = declarative_base()


# database model to store links from hackernews
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    link = Column(String(200))
    text = Column(String(200))


# helper function to save a post to the database
def save_post(session, link, text):
    post = Post(link=link, text=text)
    session.add(post)
    session.commit()
