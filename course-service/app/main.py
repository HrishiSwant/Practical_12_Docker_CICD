from fastapi import FastAPI

app = FastAPI(
    title="Course Service",
    description="Course Microservice for Practical 12",
    version="1.0.0"
)


courses = [
    {
        "id": 1,
        "name": "Computer Science"
    },
    {
        "id": 2,
        "name": "Information Technology"
    },
    {
        "id": 3,
        "name": "Data Science"
    }
]


@app.get("/")
def root():
    return {
        "message": "Course Service is running"
    }


@app.get("/courses")
def get_courses():
    return courses


@app.get("/courses/{course_id}")
def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    return {
        "message": "Course not found"
    }