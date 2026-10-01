# CRUD API
from fastapi import FastAPI ,Path ,Header ,HTTPException ,Depends
from pydantic import BaseModel

app = FastAPI()

users_db = {}
def get_db():
    print("DB connection opened")

    try:
        yield users_db
    finally:
        print("DB connection closed")

user_id = 1

class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    user_id: int
    name: str
    age: int

@app.post("/users", status_code = 201, response_model = UserResponse)
def users(user: UserCreate):
    global user_id
    id = user_id
    user_id += 1
    
    users_db[id] = {"name": user.name,"age":user.age}
    return {
        "user_id": id,
        "name": user.name,
        "age": user.age,
    }

@app.get("/users", response_model = list[UserResponse])
def get_users(users: dict = Depends(get_db)):
    return [{"user_id": id,
             "name":users[id]["name"],
             "age":users[id]["age"]}
             for id in users]

@app.get("/users/{user_id}", response_model = UserResponse)
def get_user(user_id: int = Path(...,ge=1)):
    if user_id not in users_db:
        raise HTTPException(status_code = 404, detail="User does not exists")
    
    return {"user_id": user_id,
            "name": users_db[user_id]["name"],
            "age": users_db[user_id]["age"]}
        
class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None

@app.put("/users/{user_id}" ,response_model = UserResponse)
def update_user( user_data_update: UserUpdate, user_id: int = Path(...,ge=1)):
    if user_id not in users_db: 
        raise HTTPException(status_code = 404, detail="User does not exists")
    
    if  user_data_update.name is not None:
        users_db[user_id]["name"] = user_data_update.name
    if user_data_update.age is not None:
        users_db[user_id]["age"] = user_data_update.age
    return {"user_id": user_id,
            "name": users_db[user_id]["name"],
            "age": users_db[user_id]["age"]}
    
@app.delete("/users/{user_id}", status_code = 204)
def delete_user(user_id: int = Path(...,ge=1)):
    if user_id not in users_db: 
        raise HTTPException(status_code = 404, detail="User does not exists")
    
    users_db.pop(user_id)




def get_current_user(user_id: int = Path(...,ge=1), authorization: str | None = Header(None)):
    if authorization != "Bearer my-secret-token":
        raise HTTPException(status_code=401 ,detail="Invalid or missing token")
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="user does not exists")
    return {
        "user_id": user_id,
        "name": users_db[user_id]["name"]
    }

@app.get("/profile/{user_id}")
def get_profile(user: dict = Depends(get_current_user)):
    
    return {
        "message": "Profile accessed",
        "user": user
    }

@app.get("/dashboard/{user_id}")
def get_dashboard(user: dict = Depends(get_current_user)):
    
    return {
        "message": "User dashboard",
        "user": user
    }
