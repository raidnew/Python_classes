from database import Base
import sqlalchemy as db
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

class Task(Base):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True)
    id_category = db.Column(db.ForeignKey('Category.id'))
    status = db.Column(db.Integer)
    # from 1 to 5
    #
    name = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    code = db.Column(db.String(255), unique=False, nullable=False)
    #task_students = db.relationship('TaskStudent', backref='Task')

class Category(Base):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    #tasks = db.relationship('Task', backref='Category')

class Student(Base):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    #task_students = db.relationship('TaskStudent', backref='Student')
    #group_students = db.relationship('GroupStudent', backref='Student')

class TaskStudent(Base):
    __tablename__ = 'TaskStudent'
    students = db.Column(db.ForeignKey('Student.id'), primary_key=True)
    tasks = db.Column(db.ForeignKey('Task.id'), primary_key=True)
    state = db.Column(db.Integer(), unique=False, nullable=False)
    # 0 - new
    # 1 - wait
    # 2 - resolve


class Group(Base):
    __tablename__ = 'Group'
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.ForeignKey('Teacher.id'))
    #group_students = db.relationship('GroupStudent', backref='Group')

class Teacher(Base):
    __tablename__ = 'Teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)


class GroupStudent(Base):
    __tablename__ = 'GroupStudent'
    students = db.Column(db.ForeignKey('Student.id'), primary_key=True)
    groups = db.Column(db.ForeignKey('Group.id'), primary_key=True)

class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
