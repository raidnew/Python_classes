from lab6app import teacher, models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lab6app.database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(teacher.router, tags=['Teachers'], prefix='/api/teacher')



"""

http://localhost:8000/api/teacher/

class Main():
    def __init__(self):
        models.Base.metadata.create_all(bind=engine)
        app = FastAPI()
        origins = [
            "*"
        ]
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        app.include_router(teacher.router, tags=['Teachers'], prefix='/api/teacher')

main = Main()
"""