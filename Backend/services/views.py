from django.views import View
from .serializers import *
from .models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class serviceViews(LoginRequiredMixin,View):

    def get(self,request,username):
        '''
        Method to GET Data from Server
        '''
        if services.objects.get(username = username):
            user_data = serialize("json",services.objects.filter(username = username).all())
            return user_data
        else:
            return {
                "Message" : "Data Not Found"
            }
    
    
    def post(self,request):
        
        '''
        Method to POST fresh Data to Server
        '''
        serviceform_data = UserServiceForm(request.POST or None)
        if serviceform_data.is_valid():
            fetched_data = serviceform_data.cleaned_data
            raw_user_data = ServiceModelSerializer(**fetched_data)
            obj = raw_user_data.create_service_api()
            return obj
    
    
    def patch(self,request,username):
        
        '''
        Method to UPDATE existing Data (Partial / Full)
        '''
        updateuser_data = UserServiceForm(user = username , data = request.POST or None)
        if updateuser_data.is_valid():
            fetched_data = updateuser_data.cleaned_data
            raw_user_data = ServiceModelSerializer(**fetched_data)
            obj = raw_user_data.update_service_api(username=username)
            return obj
        
    
    
    def delete(self,request,username):
        '''
        Method to DELETE an user's data
        '''
        if username and services.objects.filter(username=username):
            services.objects.filter(username=username).all().delete()
            return {
                "Message" : f"Data of {username} is deleted"
            }