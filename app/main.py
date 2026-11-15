from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(
    title="Addition API",
    description="Accepts two numbers and displays their addition via POST and GET endpoints.",
    version="1.0.0"
)


def addition(a: float, b: float) -> float:
    """Core logic to add two numbers."""
    return a + b


class NumberInput(BaseModel):
    num1: float
    num2: float


@app.get("/")
def home():
    """Welcome / root health check endpoint."""
    return {"message": "Welcome to Addition API"}


@app.post("/add")
def add_numbers_post(data: NumberInput):
    """
    POST /add endpoint: accepts JSON payload:
    {"num1": 10, "num2": 20}
    """
    result = addition(data.num1, data.num2)
    return {
        "num1": data.num1,
        "num2": data.num2,
        "addition": result
    }


@app.get("/add")
def add_numbers_get(
    num1: Optional[float] = Query(None, description="First number"),
    num2: Optional[float] = Query(None, description="Second number")
):
    """
    GET /add endpoint: allows testing in browser URL bar:
    e.g. /add?num1=10&num2=20
    """
    if num1 is None or num2 is None:
        return {
            "message": "Please provide num1 and num2 query parameters.",
            "example_url": "/add?num1=10&num2=20"
        }

    result = addition(num1, num2)
    return {
        "num1": num1,
        "num2": num2,
        "addition": result
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
