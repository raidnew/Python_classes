#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.

class Task:
    STATE_OK = "ok"
    STATE_OK_CONFIRMED = "new"
    STATE_ERROR = "error"
    STATE_IN_WORK = "inwork"
    STATE_NEW = "new"

    state = STATE_NEW
    id = 0

    def __init__(self, task_id):
        self.state = Task.STATE_IN_WORK
        self.id = task_id

    def try_solve_task(self):
        self.state = Task.STATE_OK

    def confirm_taks(self):
        #todo validate teacher caller
        if(self.state == Task.STATE_OK):
            self.state = Task.STATE_OK_CONFIRMED

    def __setattr__(self, key, value):
        if(self.state != Task.STATE_OK_CONFIRMED):
            self.__dict__[key] = value
        else:
            #task already solve
            pass

class Lesson:
    tasks:[Task]

class Pupil:
    id: 0
    tasks:[Task] #task assigned pupil

    def get_task_by_id(self, task_id):
        task:Task = tasks[0]
        return task

    def add_lesson(self, lesson:Lesson):
        #TODO ad task from lesson to pupil
        tasks += lesson.tasks[0:]
        pass

    def task_solve(self, task_id):
        get_task_by_id(task_id).try_solve_task()
        pass

    def get_task(self, task_id):
        return get_task_by_id(task_id)

class Group:
    pupils:[Pupil]
    teacher:Teacher
    id: 0

    def add_lesson(self, lesson):
        #todo add task from lessons to pupils list
        pass

class Teacher:

    groups:[Group]

    def check_task(self, group_id, pupil_id, task_id, confirm):


    pass