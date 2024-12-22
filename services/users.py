from schemas.users import UserCreate, UserUpdate, User
from database.db import users_db, books_db

 

class UserServices:

    @staticmethod
    def get_users():
        return users_db
    

    @staticmethod
    def get_user(id):
        user = user_services.get_users()
        for u in user: 
            if u["id"] == id:
                main_user = u 
                break
        return main_user                

    @staticmethod
    def create_user(user: UserCreate):
        new_user = User(id=len(user_services.get_users()) + 1, **user.model_dump())
        user.append(new_user)
        return new_user
    
    @staticmethod
    def update_user(user: User, data: UserCreate):
        user.name = data.name
        user.email = data.mail
        return user
    
    @staticmethod
    def part_update_user(user: User, data: UserUpdate):
        update_data = data.model_dump(exclude_unset=True).items()
        for key, value in update_data:
            setattr(user, key, value)
            return user
        
    @staticmethod
    def delete_user(id):
        user = user_services.get_user(id)
        user.remove(user)
        return {"message":  "user deleted!"}

    
















user_services = UserServices()

