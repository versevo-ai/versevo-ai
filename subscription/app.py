from flask import Flask , request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fakeDatabase = {
    1:{'username':'Amal1234','email':'amalxyz@gmail.com','password':'amal1234'},
    2:{'username':'Bimal!!!','email':'bimalxyz!!!!@gmil.com','password':'bimal1234!!!!'},
    3:{'username':'Suresh_coder','email':'sureshcoder@gmail.com','password':'codersuresh1234'},
}

# class emails(Resource):
#     def get(self):
#         return fakeDatabase
    
#     def post(self):
#         data = request.json
#         last_key = len(fakeDatabase.items())
#         fakeDatabase[last_key+1]={"username":data["username"], "email":data["email"], "password":data["password"]}
#         if len(fakeDatabase.items()) > last_key:
#             res = {"Status" : "Data Inserted Successfully"}
#             return res
#         else:
#             res = {"Status" : "Failed Insertion"}
#             return res
        

class email(Resource):
    def get(self,pk):
        return fakeDatabase[pk]
    
    def post(self,pk):
        if pk ==  len(fakeDatabase.keys()) + 1:
            last_length = len(fakeDatabase.items())
            data = request.json
            fakeDatabase[pk]={'username':data['username'], "email":data["email"], "password":data["password"]}
            if len(fakeDatabase.items()) > last_length:
                res = {"Status" : "Data Inserted Successfully" , "Data":fakeDatabase[pk]}
                return res
            else:
                res = {"Status" : "Failed Insertion"}
                return res
        else:
            res = {"Status" : "Failed Insertion"}
            return res
    
    def put(self,pk):
        data = request.json
        prev_data = fakeDatabase[pk]
        if data is not None:
            if data['username'] is not None and data['username'] != prev_data['username']:
                fakeDatabase[pk]['username'] = data['username']
            if data['email'] is not None and data['email'] != prev_data ['email']:
                fakeDatabase[pk]['email'] = data['email']
            if data['password'] is not None and data['password'] != prev_data ['password']:
                fakeDatabase[pk]['password'] = data['password']
            res ={
                    "Status":f"Data of Id {pk} is Updated",
                    "Data":fakeDatabase[pk]
                }
            return res
        else:
            res ={
                "Status" : "Updation Failure"
            }
            return res
    
    def delete(self,pk):
        del fakeDatabase[pk]
        res = {
            "Status" : f"Data of Id {pk} is Deleted"
        }
        return res

# api.add_resource(emails,"/")
api.add_resource(email,'/email/<int:pk>')



if __name__ == '__main__':
    app.run(debug=True)