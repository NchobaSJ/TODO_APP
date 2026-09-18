from fastapi import FastAPI

app = FastAPI(title="To-Do List API")


@app.get("/")
def read_root():
    return {"message": "To-Do API is running"}

