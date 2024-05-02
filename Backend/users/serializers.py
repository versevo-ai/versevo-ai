from django.core.serializers import serialize,deserialize
from django.core.exceptions import ValidationError
from .models import NewUser
from dotenv import load_dotenv
import os

load_dotenv()

class UserModelSerializer:
    
    '''
    This Serializer is used to Serialize Raw User's Data into REST API (JSON).
    But before going to serialize , the raw data undergoes several Validation Checks.
    '''
    def __init__(self,username,email,password,first_name,last_name) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.flag = True
        self.messagestack = []

        if self.username:
            if NewUser.objects.filter(username = self.username).count()==1:
                self.flag = False
                self.messagestack.append({
                    "Message":"Username already exists"   
                })
        else:
            self.flag = False
            self.messagestack.append({
                "Message":"Username Can't be Empty"   
            })
        
        
        if self.email:
            if NewUser.objects.filter(email = self.email).count()==1:
                self.flag = False
                self.messagestack.append({
                    "Message":"Email already exists"
                })
        else:
            self.flag = False
            self.messagestack.append({
                "Message":"Email can't be Enpty"
            })
        
        
        if self.password:
            if NewUser.objects.filter(password = self.password).count()==1:
                self.flag = False
                self.messagestack.append({
                    "Message":"Password already exists"
                })
        else:
            self.flag = False
            self.messagestack.append({
                "Message":"Password can't be empty"
            })
    
    def is_valid(self) -> bool:
        return self.flag
    
    def Get_Jwt_Tokens(self) -> dict:
        
        # Some Code that will generate Bearer and Refresh Token Here
        
        Tokens=dict()
        return Tokens
    
    def create_user_api(self):
        if self.email == os.getenv("SUPERUSER_EMAIL"):
            userobj = NewUser.objects.create_superuser(username = self.username , email = self.email , password = self.password)
        else:
            userobj = NewUser.objects.create_user(username = self.username , email = self.email)
        Tokens = self.Get_Jwt_Tokens()
        userobj.Bearer_Token = Tokens.get("Bearer_Token")
        userobj.Refresh_Token = Tokens.get("Refresh_Token")
        user_api = serialize("json",userobj)
        return user_api
    
    
    def update_user_api(self,username):
        userobj = NewUser.objects.get(username = username)
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
        
        
    
    
    
        
    

