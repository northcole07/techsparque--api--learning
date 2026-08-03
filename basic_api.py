from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def home():
    return{"message": "Welcome to my API"}
@app.get("/students")
def students():
    return{
        "students":[
            "Alan",
            "Misha",
            "Sasha",
            ]
        }
@app.get("/topics")
def topics():
    return{
        "topics": [
            "Python",
            "FastAPI",
            "JSON"
            ]
        }
