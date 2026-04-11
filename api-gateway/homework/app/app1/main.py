# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_root():
    return {"app_name": "APP1","status": "success", "message": "Method GET API is running behind NGINX"}
@app.post("/api")
def read_root():
    return {"app_name": "APP1","status": "success", "message": "Method POST API is running behind NGINX"}
@app.put("/api")
def read_root():
    return {"app_name": "APP1","status": "success", "message": "Method PUT API is running behind NGINX"}
@app.delete("/api")
def read_root():
    return {"app_name": "APP1","status": "success", "message": "Method DELETE API is running behind NGINX"}
