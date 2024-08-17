import datetime
from django.core.serializers import serialize
from .models import NewUser
from django.core.exceptions import ValidationError
from dotenv import load_dotenv
from django.http import JsonResponse
import string
import os

load_dotenv()


class UserModelSerializer:
    """
    This Serializer is used to Serialize Raw User's Data into REST API (JSON).
    But before going to serialize , the raw data undergoes several Validation Checks.
    """

    def __init__(self, username:str, method:str, email:str=None, password1:str=None, password2:str=None, first_name:str=None, last_name:str=None) -> list:
        self.username = username
        self.method = method
        self.email = email
        self.password1 = password1
        self.password2 = password2
        self.first_name = first_name
        self.last_name = last_name
        self.messagestack = []

        if self.username:
            if NewUser.objects.filter(username=self.username).count() == 1:
                self.messagestack.append({"Message": "Username already exists"})
        else:
            self.messagestack.append({"Message": "Username Can't be Empty"})

        if self.email:
            if NewUser.objects.filter(email=self.email).count() == 1:
                self.messagestack.append({"Message": "Email already exists"})
        else:
            self.messagestack.append({"Message": "Email can't be Enpty"})
        
        return self.set_password()
        
    
    def set_password(self):
        smalls = list(string.ascii_lowercase)
        caps = list(string.ascii_uppercase)
        symbols = list(string.punctuation)
        digits = list(string.digits)
        if (not self.password1) or (not self.password2):
            self.messagestack.append({"Message":"Password Field Can't be Empty"})
            return JsonResponse(self.throw_errorlist())
        elif self.password1 != self.password2:
            self.messagestack.append({"Message":"Passwords Should Match"})
            return JsonResponse(self.throw_errorlist())
        elif len(self.password1)<8 or len(self.password1)<8:
            self.messagestack.append({"Message":"Minimum length of password is 8"})
            return JsonResponse(self.throw_errorlist())
        else:
            list_pass = list(self.password1)
            status_queue = [0,0,0,0]
            for i in list_pass:
                if i in smalls:
                    status_queue[0]=1
                elif i in caps:
                    status_queue[1]=1
                elif i in symbols:
                    status_queue[2]=1
                elif i in digits:
                    status_queue[3]=1
                if status_queue == [1,1,1,1]:
                    break
            if status_queue[0]==0:
                self.messagestack.append({"Message":"Atleast One Small Letter Is Needed"})
            if status_queue[1]==0:
                self.messagestack.append({"Message":"Atleast One Capital Letter Is Needed"})
            if status_queue[2]==0:
                self.messagestack.append({"Message":"Atleast One Symbol Is Needed"})
            if status_queue[3]==0:
                self.messagestack.append({"Message":"Atleast One digit Is Needed"})
            return JsonResponse(self.throw_errorlist())

    
    def throw_errorlist(self)->list:
        return self.messagestack

    def create_user_api(self):
        temp = self.messagestack
        del temp
        self.messagestack = []
        if self.method in ['POST','post']:
            if self.email == os.getenv("SUPERUSER_EMAIL"):
                userobj = NewUser.objects.create_superuser(
                    username=self.username, email=self.email, password=self.password1
                )
            else:
                userobj = NewUser.objects.create_user(
                    username=self.username, email=self.email, password=self.password1
                )
            userobj.first_name = self.first_name
            userobj.last_name = self.last_name
            userobj.save()
        # Seperate Module will come for this

        # Tokens = self.Get_Jwt_Tokens()
        # userobj.Access_Token = Tokens.get("Access_Token")
        # userobj.Refresh_Token = Tokens.get("Refresh_Token")
        # userobj.private_key = Tokens.get("private_key")
        # userobj.public_key = Tokens.get("public_key")

            user_api = serialize("json", userobj)
            return user_api
        else:
            self.messagestack.append({"Message":"Object already exists in Database"})
            return JsonResponse(self.throw_errorlist())

    def update_user_api(self,username):
        temp = self.messagestack
        del temp
        self.messagestack = []
        if username!= None and self.method in ['PUT','put','PATCH','patch']:
            obj = NewUser.objects.get(username=username)
            if NewUser.objects.filter(username=username).exists() == True and obj.Blacklisted == False:
                if obj.username != self.username:
                    obj.username = self.username
                if obj.email != self.email:
                    obj.email = self.email
                if obj.first_name != self.first_name:
                    obj.first_name = self.first_name  
                if obj.last_name != self.last_name:
                    obj.last_name = self.last_name
                if obj.password != self.password1:
                    obj.password = self.password1
                obj.save()
                user_api = serialize("json", obj)
                return user_api
            else:
                self.messagestack.append({"Message": "This User is Blacklisted"})
                return JsonResponse(self.throw_errorlist())
        else:
            self.messagestack.append({"Message":"Object does not exists in Database"})
            return JsonResponse(self.throw_errorlist())
