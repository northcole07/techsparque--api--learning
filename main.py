from fastapi import FastAPI
app = FastAPI()
students = [
    {
        "id": 1,
        "name": "Alice",
        "topic": "Python",
        "completed": True,
        "notes": "Completed Python basics."
    },
    {
        "id": 2,
        "name": "Brian",
        "topic": "FastAPI",
        "completed": False,
        "notes": "Learning API routes."
    }
]

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student
    return {"message":"Student not found"}

topics = [
    {"topic": "Python", "completed": True},
    {"topic": "Github", "completed": True},
    {"topic": "Backend", "completed": False},
    {"topic": "Vibe Coding", "completed": False}
    ]

@app.get("/topics")
def get_topics():
    return topics
