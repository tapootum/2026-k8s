# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def read_root():
    return {"app_name": "APP2","status": "success", "message": "Method GET API is running behind NGINX"}
@app.post("/user")
def read_root():
    return {"app_name": "APP2","status": "success", "message": "Method POST API is running behind NGINX"}
@app.put("/user")
def read_root():
    return {"app_name": "APP2","status": "success", "message": "Method PUT API is running behind NGINX"}
@app.delete("/user")
def read_root():
    return {"app_name": "APP2","status": "success", "message": "Method DELETE API is running behind NGINX"}
