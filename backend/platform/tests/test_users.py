from django.http import JsonResponse
from django.test import Client
from django.urls import reverse
import pytest
from services.models import *
from services.serializers import *
from services.forms import *
from django.core.exceptions import ValidationError


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
        TestDatabase = {}
        return TestDatabase
    
    
    @pytest.fixture(scope="function")
    def test_create_data(self,**data):
        '''
        A mock fixture method to serialize the raw data into a dict
        '''
        uname = data.get("username")
        if not self.get_test_database()[uname]:
            return {
                'username' : data.get("username"),
                'email' : data.get("email"),
                'password' : data.get("password"),
                'first_name' : data.get("first_name"),
                'last_name' : data.get("last_name")
            }
        else:
            return False
        
    @pytest.fixture(scope="function")
    def test_create_api(self,**data):
        '''
        A mock fixture method to serialize the dictionary data into an JSON based REST API
        '''
        if self.test_create_data(data=data):
            obj = serialize("json",self.test_create_data(data=data)) # type: ignore
            self.get_test_database()[obj.username] = obj
            return obj
        else:
            raise ValidationError({
                "Message":"Data already Exists"
            })
    
    @pytest.fixture(scope="function")
    def test_update_api(self,username,**data):
        '''
        A mock fixture method to update any data
        '''
        new_obj =  self.test_create_data(data=data)
        if new_obj:
            old_obj = self.get_test_database()[username]
            # if new_obj['username'] != old_obj['username']:
            #     old_obj['username'] = new_obj['username']
            #     self.get_test_database()[username] = old_obj

            if new_obj['email'] != old_obj['email']:
                old_obj['email'] = new_obj['email']
                
            if new_obj['password'] != old_obj['password']:
                old_obj['password'] = new_obj['password']
                
            if new_obj['first_name'] != old_obj['first_name']:
                old_obj['first_name'] = new_obj['first_name']
                
            if new_obj['last_name'] != old_obj['last_name']:
                old_obj['last_name'] = new_obj['last_name']
                
            return old_obj
        
    
    def test_get_method(self):
        '''
        Testcase for applying GET request on the testdatabase
        '''
        response = self.client().get(reverse('get_test_database'))
        print(response.content)
        assert response.status_code == 200
    
    def test_post_method(self):
        '''
        Testcase for applying POST request on the testdatabase
        '''
        entrycount = len(self.get_test_database().keys())
        data = send_data_to_testclass()
        response = self.client().post(reverse("test_create_api"),data=data,format="json")
        entrycount += 1
        assert response.status_code == 201 and entrycount == len(self.get_test_database().keys())
    
    def test_patch_method(self):
        '''
        Testcase for applying PATCH request on the testdatabase
        '''
        db = self.get_test_database()
        data = send_data_to_testclass()
        username = data['username']
        if username in db.keys():
            oldcontent = db[username]
            response = self.client().patch(reverse("test_update_api"),data=data,format="json")
            assert response.status_code == 200 and oldcontent != response.content
    
    def test_delete_method(self):
        '''
        Testcase for applying DELETE request on the testdatabase
        '''
        db = self.get_test_database()
        entriescount = len(db.keys())
        obj = send_data_to_testclass()
        username = obj.get("username")
        if username in db.keys():
            del db[username]
            del obj
            entriescount -= 1
            assert entriescount == len(db.keys())
    
    def teardown_method(self):
        del self
        return JsonResponse({
            "Message" : "Testsuit executed successfully"
        })      

def send_data_to_testclass()->dict:
    username , email , password , first_name , last_name = tuple(input().split(" "))
    return {
        "username":username or None,
        "email":email or None,
        "password":password or None,
        "first_name":first_name or None,
        "last_name":last_name or None
    }

            