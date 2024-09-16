from django.http import JsonResponse
from django.test import Client
import pytest
from services.models import *
from services.serializers import *
from services.forms import *
from users.models import *
from users.serializers import *

@pytest.mark.django_db
class TestUsers:
    @pytest.fixture(scope="function")
    def client(self):
        ''' 
        A fixture Testclient method which provides all HTTP Methods
        '''
        return Client()
    
    
    @pytest.fixture(scope="function")
    def get_test_database(self):
        '''
        A fixture method to get the mock or fake database
        '''
        return NewUser.objects.all()

        
    @pytest.fixture(scope="function")
    def test_create_object(self,**data):
        '''
        A mock fixture method to serialize the dictionary data into an JSON based REST API
        '''
        serializer = UserModelSerializer(**data)
        if serializer==[]:
            res = serializer.create_user_api()
            return res # May return errors caused in Creating Api
        else:
            return serializer # return errors caused while validating data
    
    @pytest.fixture(scope="function")
    def test_update_object(self,username,**data):
        '''
        A mock fixture method to update any data
        '''
        serializer = UserModelSerializer(**data)
        if serializer==[]:
            res = serializer.update_user_api(username=username)
            return res # May return errors caused in Updating Api
        else:
            return serializer # return errors caused while validating data
    
    def test_get_method(self):
        '''
        Testcase for applying GET request on the testdatabase
        '''
        return self.get_test_database()
    
    
    def test_post_method(self,**data): 
        '''
        Testcase for applying POST request on the testdatabase
        '''
        return self.test_create_object(data=data)
    
    def test_patch_method(self,username,**data):
        '''
        Testcase for applying PATCH request on the testdatabase
        '''
        return self.test_update_object(username=username,data=data)
    
    def test_delete_method(self,username):
        '''
        Testcase for applying DELETE request on the testdatabase
        '''
        NewUser.objects.filter(username=username).all().delete()
        return JsonResponse({"Message":f"Object of Username {username} deleted"})
    
    def teardown_method(self):
        del self
        return JsonResponse({
            "Message" : "Testsuit executed successfully"
        })      
            