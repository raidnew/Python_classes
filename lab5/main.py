import models, teacher, user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    #"http://localhost:3000",
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
app.include_router(user.router, tags=['Users'], prefix='/api/user')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}