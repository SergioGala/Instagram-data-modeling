import os
import sys
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    nombre = Column(String(50))
    bio = Column(String(250))
    fecha_registro = Column(DateTime)
    
    posts = relationship("Post", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    likes = relationship("Like", back_populates="usuario")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    imagen_url = Column(String(250), nullable=False)
    caption = Column(String(250))
    fecha_publicacion = Column(DateTime)
    
    usuario = relationship("Usuario", back_populates="posts")
    comentarios = relationship("Comentario", back_populates="post")
    likes = relationship("Like", back_populates="post")

class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    texto = Column(String(250), nullable=False)
    fecha_comentario = Column(DateTime)
    
    usuario = relationship("Usuario", back_populates="comentarios")
    post = relationship("Post", back_populates="comentarios")

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    fecha_like = Column(DateTime)
    
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    description= Column(String(25000))
    user_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))
    
    usuario = relationship("Usuario", back_populates="likes")
    post = relationship("Post", back_populates="likes")

    render_er(Base, 'diagram.png')
    