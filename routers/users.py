from fastapi import APIRouter, HTTPException
from services.users import user_services
from schemas.users import UserCreate, UserUpdate



user_router = APIRouter()
# user_new = UserCrud()


    


@user_router.get("/")
def get_users():
     users = user_services.get_users()
     return users
     

@user_router.get("/{id}")
def get_user(id: int): 
    user = user_services.get_user(id)
    return user


@user_router.post("/")
def create_user(payload: UserCreate):
     new_user = user_services.create_user(payload)
     return new_user

@user_router.put("/{id}")
def update_user(id:int, payload:UserCreate):
     user = user_services.get_user(id)
     updated_user = user_services.update_user(user=user, data=payload)
     return updated_user


@user_router.patch("/{id}")
def part_update_user(id:int, payload:UserUpdate):
     user = user_services.get_users(id)
     part_update_user = user_services.part_update_user(user=user, data=payload)
     return part_update_user

@user_router.delete("/{id}")
def delete_user(id: int):
     user_services.delete_user(id)





# @user_router.get("/{user_id}", response_model=User)
# def get_user(user_id: int):
#     user = next ((u for u in users_db if u.id == user_id), None)
#     if not user:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return user

# @user_router.post("/", response_model=User)
# def create_user(user: User):
#     if any(u["id"] == user.id for u in users_db):
#         raise HTTPException(status_code=400, detail="User with this ID already exists")
#     users_db.append(user.dict())
#     return user


# def update_user(user_id: int, updated_user: User):
#     for index, user in enumerate(users_db):
#         if user["id"] == user_id:
#             users_db[index] = updated_user.dict()
#             return updated_user
#     raise HTTPException(status_code=404, detail="User not found")


# @user_router.delete("/{user_id}")
# def delete_user(user_id: int):
#     for user in users_db:
#         if user["id"] == user_id:
#             users_db.remove(user)
#             return {"message": f"User with ID {user_id} deleted successfully"}
#     raise HTTPException(status_code=404, detail="User not found")


# @user_router.put("/{user_id}/deactivate")
# def deactivate_user(user_id: int):
#     for user in users_db:
#         if user["id"] == user_id:
#             user["is_active"] = False
#             return {"message": f"User with ID {user_id} has been deactivated"}
#     raise HTTPException(status_code=404, detail="User not found")
