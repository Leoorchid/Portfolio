from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    subject: str


students = {
    1: {
        "name": "spongebob",
        "age": 20,
        "subject": "cooking",
    },
    2: {
        "name": "patrick",
        "age": 19,
        "subject": "R&R",
    },
    3: {
        "name": "sandy",
        "age": 21,
        "subject": "sicence",
    },
}


@app.get("/")
def root():
    return {"message": "hello world"}


@app.get("/students/{studentId}")
def getStudents(studentId: int = Path(..., description="The ID of the student", gt=1)):
    return students[studentId]


@app.get("/studentName")
def getStudentName(name: str):
    for student in students:
        if students[student]["name"] == name:
            return students[student]


@app.post("/postStudent")
def add_Student(student: Student):
    student_id = len(students) + 1
    student[student_id] = student.dict()
    return {"id": student_id, "student": student}
