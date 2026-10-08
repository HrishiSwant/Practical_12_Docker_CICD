from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI(
    title="API Gateway",
    description="API Gateway for Practical 12",
    version="1.0.0"
)


# Service URLs
STUDENT_SERVICE_URL = os.getenv(
    "STUDENT_SERVICE_URL",
    "http://127.0.0.1:8001"
)

COURSE_SERVICE_URL = os.getenv(
    "COURSE_SERVICE_URL",
    "http://127.0.0.1:8002"
)


@app.get("/")
def root():
    return {
        "message": "API Gateway is running"
    }


@app.get("/students")
def get_students():

    try:
        response = httpx.get(
            f"{STUDENT_SERVICE_URL}/students",
            timeout=5.0
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Student Service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Student Service unavailable"
        )


@app.get("/students/{student_id}")
def get_student(student_id: int):

    try:
        response = httpx.get(
            f"{STUDENT_SERVICE_URL}/students/{student_id}",
            timeout=5.0
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Student Service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Student Service unavailable"
        )


@app.get("/courses")
def get_courses():

    try:
        response = httpx.get(
            f"{COURSE_SERVICE_URL}/courses",
            timeout=5.0
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Course Service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Course Service unavailable"
        )


@app.get("/courses/{course_id}")
def get_course(course_id: int):

    try:
        response = httpx.get(
            f"{COURSE_SERVICE_URL}/courses/{course_id}",
            timeout=5.0
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Course Service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Course Service unavailable"
        )