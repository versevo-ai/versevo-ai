from django.http import JsonResponse
from django.test import Client
from django.urls import reverse
import pytest
from services.models import *
from services.serializers import *
from services.forms import *

class TestServices:
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
        return {
            'username' : data.get("username"),
            'money' : data.get("money"),
            'text_to_speech' : data.get("text_to_speech"),
            'speech_to_text' : data.get("speech_to_text"),
            'speech_to_speech' : data.get("speech_to_speech")
        }
    
    @pytest.fixture(scope="function")
    def test_create_api(self,**data):
        '''
        A mock fixture method to serialize the dictionary data into an JSON based REST API
        '''
        obj = serialize("json",self.test_create_data(data=data)) # type: ignore
        self.get_test_database()[obj.username] = obj
        return obj
    
    @pytest.fixture(scope="function")
    def test_update_api(self,username,**data):
        '''
        A mock fixture method to update any data
        '''
        new_obj =  self.test_create_data(data=data)
        old_obj = self.get_test_database()[username]
        # if new_obj['username'] != old_obj['username']:
        #     old_obj['username'] = new_obj['username']
        #     self.get_test_database()[username] = old_obj

        if new_obj['money'] != old_obj['money']:
            old_obj['money'] = new_obj['money']
            
        if new_obj['text_to_speech'] != old_obj['text_to_speech']:
            old_obj['text_to_speech'] = new_obj['text_to_speech']
            
        if new_obj['speech_to_text'] != old_obj['speech_to_text']:
            old_obj['speech_to_text'] = new_obj['speech_to_text']
            
        if new_obj['speech_to_speech'] != old_obj['speech_to_speech']:
            old_obj['speech_to_speech'] = new_obj['speech_to_speech']
        
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
            response = self.client().patch(reverse("test_update_api"),kwargs={"username":username},data=data,format="json") # type: ignore
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
    username , money , text_to_speech , speech_to_text , speech_to_speech = tuple(input().split(" "))
    return {
        "username":username or None,
        "money":money or None,
        "text_to_speech":text_to_speech or None,
        "speech_to_text":speech_to_text or None,
        "speech_to_speech":speech_to_speech or None
    }
      
            
                
        
        
    
        
    
    