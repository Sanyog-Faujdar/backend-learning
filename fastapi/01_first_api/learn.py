from fastapi import FastAPI ,HTTPException ,Query ,Path ,Header

from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    name: str
    age: int

class UserCreated(BaseModel):
    user_id: int
    name: str
    age: int
    send_email: bool


@app.get("/")
def home_page():
    return {"message": "hello from my API"}

@app.get("/users/{user_id}")
def users(user_id: int = Path(..., ge=1), ):
    return {
        "user_id": user_id,
        "message": "User found"        
    }

@app.get("/users")
def users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1 ,le=100)):
    return {
        "page": page,
        "limit": limit,
        "message": "Users fetched"
    }


@app.post("/users", response_model = UserResponse)
def create_users(user: UserCreate):
    return {
        "name": user.name,
        "age": user.age,
        "message": "User created"
    }

@app.post("/users/{user_id}", response_model = UserCreated)
def user_email(user: UserCreate, user_id: int, send_email: bool = False):
    return {
        "user_id": user_id,
        "name": user.name,
        "age": user.age,
        "send_email": send_email
    }

@app.post("/user", status_code=201)
def create_user(user: UserCreate):
    return {
        "name": user.name,
        "age": user.age
    }

users_db = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

class CheckUser(BaseModel):
    name: str
    age: int

@app.get("/users/{user_id}" ,response_model = CheckUser)
def get_user(user_id: int):
    if not (user_id in users_db):
        raise HTTPException(status_code = 404, detail = "User not found")
    user = users_db[user_id]
    return {
        "name": user["name"],
        "age": user["age"]
    }

@app.get("/profile")
def get_profile(authorization: str | None = Header(None, alias="Authorization")):
    print(repr(authorization))
    if authorization != "Bearer my-secret-token":
        raise HTTPException(status_code=401 ,detail="Invalid or missing token")
    return {
        "message": "Profile accessed"
    }


class Posts(BaseModel):
    user_id: int
    page: int
    message: str

@app.get("/users/{user_id}/posts" ,response_model = Posts)
def users_posts(user_id: int = Path(...,ge = 1), 
                page: int = Query(1,ge=1),
                authorization: str | None = Header(None)):
    
    if authorization != "Bearer my-secret-token":
        raise HTTPException(status_code=401 ,detail="Invalid or missing token")
    return {
        "user_id": user_id,
        "page": page,
        "message": "posts fetched"
    }

@app.get("/admin")
def admin(authorization : str|None = Header(None)):
    
    if authorization == "Bearer admin-token":
        return {"message": "hello admin"}
    elif authorization == "Bearer user-token":
        raise HTTPException(status_code=403 ,detail="Not admin")
    else:
        raise HTTPException(status_code=401 ,detail="Invalid or missing token") 