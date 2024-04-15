from django.core.serializers import serialize,deserialize
from django.core.exceptions import ValidationError
from .models import NewUser
from dotenv import load_dotenv
import os

load_dotenv()

class UserModelSerializer:
    def __init__(self,username,email,password,first_name,last_name) -> None:
        self.model = NewUser
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

        if self.username:
            if self.model.objects.filter(username = self.username).count()==1:
                raise ValidationError(f"Username already exists")
        else:
            raise ValidationError("Username Can't be Empty")
        
        
        if self.email:
            if self.model.objects.filter(email = self.email).count()==1:
                raise ValidationError(f"Email already exists")
        else:
            raise ValidationError("Email Can't be Empty")
        
        
        if self.password:
            if self.model.objects.filter(password = self.password).count()==1:
                raise ValidationError(f"This Password is already Chosen")
        else:
            raise ValidationError("Password Can't be Empty")
    
    def Get_Jwt_Tokens(self) -> dict:
        
        # Some Code that will generate Bearer and Refresh Token Here
        
        Tokens=dict()
        return Tokens
    
    def create_user_api(self):
        if self.email == os.getenv("SUPERUSER_EMAIL"):
            userobj = self.model.objects.create_superuser(username = self.username , email = self.email , password = self.password)
        else:
            userobj = self.model.objects.create_user(username = self.username , email = self.email)
        Tokens = self.Get_Jwt_Tokens()
        userobj.Bearer_Token = Tokens.get("Bearer_Token")
        userobj.Refresh_Token = Tokens.get("Refresh_Token")
        userobj.save()
        user_api = serialize("json",userobj)
        return user_api
    
    
    def update_user_api(self,username):
        userobj = self.model.objects.get(username = username)
        if userobj.username != self.username:
            userobj.username = self.username
        if userobj.email != self.email:
            userobj.email = self.email
        if userobj.first_name != self.first_name:
            userobj.first_name = self.first_name
        if userobj.last_name != self.last_name:
            userobj.last_name = self.last_name
        userobj.save()
        user_api = serialize("json",userobj) 
        return user_api
        
        
    
    
    
        
    

