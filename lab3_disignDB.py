#todo:
# Для модели вашего варианта БД создать ORM модель в SQLAlchemy. Сгенерировать ее в БД.
# Переписать запросы с SQL на ORM.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zzzzxxxx@localhost:5432'
app.app_context().push()
db = SQLAlchemy(app)
#metadata = db.MetaData()

class Child(db.Model):
    __tablename__ = 'child'
    id = db.Column(db.Integer, primary_key=True)
    id_group = db.Column(db.ForeignKey('group.id'))
    name = db.Column(db.String(255), unique=False, nullable=False)

class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    childs = db.relationship('Child', backref='Group')
    schedule_groups = db.relationship('ScheduleGroup', backref='Group')
    id_class_teacher = db.Column(db.ForeignKey('teacher.id'))
    level = db.Column(db.Integer, unique=False, nullable=False)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    group = db.relationship('Group', backref='Teacher')
    subject = db.relationship('Subject', backref='Teacher')
    name = db.Column(db.String(255), unique=False, nullable=False)

class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    mark = db.relationship('Mark', backref='Subject')
    schedule  = db.relationship('Schedule', backref='Subject')
    id_teacher = db.Column(db.ForeignKey('teacher.id'), primary_key=True, unique=True)

class Mark(db.Model):
    __tablename__ = 'mark'
    id = db.Column(db.Integer, primary_key=True)
    id_child = db.Column(db.ForeignKey('child.id'), primary_key=True)
    id_subject = db.Column(db.ForeignKey('subject.id'), primary_key=True)
    mark_value = db.Column(db.Integer, unique=False, nullable=False)
    id_schedule = db.Column(db.ForeignKey('schedule.id'), primary_key=True)
    description = db.Column(db.String(255), unique=False, nullable=True)

class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    mark = db.relationship('Mark', backref='Schedule')
    id_subject = db.Column(db.ForeignKey('subject.id'), primary_key=True)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    schedule_groups = db.relationship('ScheduleGroup', backref='Schedule')


class ScheduleGroup(db.Model):
    __tablename__ = 'schedulegroup'
    schedules = db.Column(db.ForeignKey('schedule.id'), primary_key=True)
    groups = db.Column(db.ForeignKey('group.id'), primary_key=True)

db.create_all()
