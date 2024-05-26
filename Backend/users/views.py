from django.views import View
from .serializers import *
from .models import *
from services.models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login ,authenticate , logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
import jwt

# Create your views here.

class userViews(View):

    def get(self,request,username):
        
        '''
        Method to GET Data from Server
        '''
        
        # Tokens will be fetched from Security Module and then verification will be done in GET Request
        
        if NewUser.objects.get(username = username):
            user_data = serialize("json",NewUser.objects.filter(username=username).all())
            return user_data
        else:
            raise ValueError({"Message" : "No User Exists"})
    
    
    def post(self,request):
        
        '''
        Method to POST fresh Data to Server
        '''
        userform_data = UserForm(request.POST or None)
        if userform_data.is_valid():
            password = userform_data.clean_password2()
            fetched_data = userform_data.cleaned_data
            raw_user_data = UserModelSerializer(
                username=fetched_data.get("username"),
                email=fetched_data.get("email"),
                password=password,
                first_name=fetched_data.get("first_name"),
                last_name=fetched_data.get("last_name")
            )
            if raw_user_data.is_valid():
                obj = raw_user_data.create_user_api()
                user_obj = NewUser.objects.filter(username = fetched_data.get("username")).all()
                login(request,user_obj)
                return obj
            else:
                raise raw_user_data.messagestack
    
    
    def patch(self,request):
        
        '''
        Method to UPDATE existing Data (Partial / Full)
        '''
        if request.user is not None:
            updateuser_data = updateUserForm(user = request.user , data = request.POST or None)
            if updateuser_data.is_valid():
                fetched_data = updateuser_data.cleaned_data
                raw_user_data = UserModelSerializer(**fetched_data)
                if raw_user_data.is_valid():
                    obj = raw_user_data.update_user_api()
                    return obj
                else:
                    raise raw_user_data.messagestack
        else:
            obj = {
                "Message" : "No User Exists"
            }
            raise ValueError(obj)
        
    
    
    def delete(self,request):
        '''
        Method to DELETE an user's data
        '''
        if request.user is not None:
            uname = request.user.username
            if NewUser.objects.get(username = uname).Blacklisted:
                NewUser.objects.filter(username = uname).all().delete()
                logout(request)
                return {
                    "Message" : f"User Object of Username {uname} is deleted"
                }
        else:
            obj = {
                "Message" : "No User Exists"
            }
            raise ValueError(obj)
    

class PasswordView(LoginRequiredMixin , View):
    
    def patch(self , request):
        if request.user is not None:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
            else:
                return {
                    "Message" : "Password is not Valid"
                }
        else:
            obj = {
                "Message" : "No User Exists"
            }
            return ValueError(obj)