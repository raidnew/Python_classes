from lab6app.database import Base
import sqlalchemy as db

class Task(Base):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True)
    id_category = db.Column(db.ForeignKey('Category.id'))
    status = db.Column(db.Integer)
    name = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    code = db.Column(db.String(255), unique=False, nullable=False)

class Category(Base):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)

class Student(Base):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)

class TaskStudent(Base):
    __tablename__ = 'TaskStudent'
    students = db.Column(db.ForeignKey('Student.id'), primary_key=True)
    tasks = db.Column(db.ForeignKey('Task.id'), primary_key=True)
    state = db.Column(db.Integer(), unique=False, nullable=False)

class Group(Base):
    __tablename__ = 'Group'
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.ForeignKey('Teacher.id'))

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
