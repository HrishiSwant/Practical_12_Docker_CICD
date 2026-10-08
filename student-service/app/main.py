from fastapi import FastAPI

app = FastAPI(
    title="Student Service",
    description="Student Microservice for Practical 12",
    version="1.0.0"
)


students = [
    {
        "id": 1,
        "name": "Rahul",
        "course_id": 1
    },
    {
        "id": 2,
        "name": "Priya",
        "course_id": 2
    },
    {
        "id": 3,
        "name": "Amit",
        "course_id": 1
    }
]


@app.get("/")
def root():
    return {
        "message": "Student Service is running"
    }


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {
        "message": "Student not found"
    }