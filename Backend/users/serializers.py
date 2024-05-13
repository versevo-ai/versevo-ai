import datetime
from django.core.serializers import serialize,deserialize
from django.core.exceptions import ValidationError
from .models import NewUser
from dotenv import load_dotenv
import os
import jwt
import uuid
import random

load_dotenv()

class UserModelSerializer:
    
    '''
    This Serializer is used to Serialize Raw User's Data into REST API (JSON).
    But before going to serialize , the raw data undergoes several Validation Checks.
    '''
    def __init__(self,username,email,password,first_name=None,last_name=None) -> None:
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
        private_key = "".join([str(uuid.uuid5) for _ in range(50)]) + "".join([random.randint(a=1,b=10) for _ in range(10)]) + "".join([str(uuid.uuid5) for _ in range(50)])
        public_key = "".join([str(uuid.uuid3) for _ in range(1000)]) + "".join([random.randint(a=1,b=100) for _ in range(10)])
        
        payload = {
            "username":self.username,
            "email":self.email,
            "password":self.password
        }
        
        # payload["exp"] = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=15)
        access_token = jwt.encode(payload=payload,key=public_key,algorithm="RS256")
        
        payload["exp"] = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=40)
        refresh_token = jwt.encode(payload=payload,key=public_key,algorithm="RS256")
        
        Tokens_n_keys={
            "Access_Token":access_token,
            "Refresh_Token":refresh_token,
            "private_key":private_key,
            "public_key":public_key
        }
        return Tokens_n_keys
    
    def create_user_api(self):
        if self.email == os.getenv("SUPERUSER_EMAIL"):
            userobj = NewUser.objects.create_superuser(username = self.username , email = self.email , password = self.password)
        else:
            userobj = NewUser.objects.create_user(username = self.username , email = self.email)
        Tokens = self.Get_Jwt_Tokens()
        userobj.Access_Token = Tokens.get("Access_Token")
        userobj.Refresh_Token = Tokens.get("Refresh_Token")
        userobj.private_key = Tokens.get("private_key")
        userobj.public_key = Tokens.get("public_key")
        user_api = serialize("json",userobj)
        return user_api
    
    
    def update_user_api(self,username):
        if NewUser.objects.get(username=username).Blacklisted == False:
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
        else:
            self.messagestack = []
            self.messagestack.append({
                "Message" : "This User is Blacklisted"
            })
            
        
        
    
    
    
        
    

