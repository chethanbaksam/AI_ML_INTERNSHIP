from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "division": a / b
    }