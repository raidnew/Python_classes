from datetime import datetime
from typing import List
from pydantic import BaseModel

class Task(BaseModel):
    id = str
    id_category = int
    status = str
    name = str
    description = str
    code = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Category(BaseModel):
    id = str
    name = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Student(BaseModel):
    id = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class TaskStudent(BaseModel):
    students = str
    tasks = str
    state = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Group(BaseModel):
    id = str
    teacher = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Teacher(BaseModel):
    id = str
    name = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class GroupStudent(BaseModel):
    students = str
    groups = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class User(BaseModel):
    id = str
    username = str
    email = str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
