from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1: {"name": "Chethan", "age": 19},
    2: {"name": "Rahul", "age": 20},
    3: {"name": "Ananya", "age": 18}
}

@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    raise HTTPException(status_code=404, detail="Student not found")