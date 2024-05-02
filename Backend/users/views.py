from django.http import HttpResponse
from django.views import View
from .serializers import *
from .models import *
from .forms import *
from django.core.serializers import serialize

# Create your views here.

class userViews(View):

    def get(self,request,username):
        '''
        Method to GET Data from Server
        '''
        if username is None:
            user_data = serialize("json",NewUser.objects.all())
            return user_data
        elif NewUser.objects.get(username = username):
            user_data = serialize("json",NewUser.objects.filter(username = username).all())
            return user_data
        else:
            return {
                "Message" : "Data Not Found"
            }
    
    
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
                return obj
            else:
                raw_user_data.messagestack
    
    
    def patch(self,request,username):
        '''
        Method to UPDATE existing Data (Partial / Full)
        
        '''
        updateuser_data = updateUserForm(request.POST or None)
        if updateuser_data.is_valid():
            fetched_data = updateuser_data.cleaned_data
            raw_user_data = UserModelSerializer(
                username=fetched_data.get("username"),
                email=fetched_data.get("email"),
                first_name=fetched_data.get("first_name"),
                last_name=fetched_data.get("last_name")
            )
            if raw_user_data.is_valid():
                obj = raw_user_data.update_user_api()
                return obj
            else:
                raw_user_data.messagestack
        return HttpResponse("result")
    
    
    def delete(self,request):
        return HttpResponse("result")