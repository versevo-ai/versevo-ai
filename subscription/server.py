from flask_restful import Resource,marshal_with
from models import app , emailSerializer , emailModel , api , db
from flask import request


# import os
# from flask_mail import Mail, Message
# from dotenv import load_dotenv

# load_dotenv()

# mail = Mail(app)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = os.getenv("ADMIN_EMAIL")
# app.config['MAIL_PASSWORD'] = os.getenv("ADMIN_EMAIL_PASSWORD")
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True


class emails(Resource):
    # @marshal_with(emailSerializer)
    # NOW PK IS GONE !! DO THE GET METHOD USING emails as PK
    # def get(self,pk):
    #     """
    #     View Logic For Get Request
    #     """
    #     if pk == 0:
    #         email_datas =  emailModel.query.all()
    #         return email_datas
    #     elif emailModel.query.filter_by(id = pk).count() == 1:
    #         email_data = emailModel.query.filter_by(id = pk).all()
    #         return email_data
    #     else:
    #         return {"Status": "Data Not Found"}
    
    @marshal_with(emailSerializer)
    def post(self):
        try:
            data = request.json
            email_data = emailModel(email = data['email'])
            db.session.add(email_data)
            db.session.commit()
            res = {
                "Status" : "Insertion Successfull",
                "Data(Email)" : emailModel.query.filter_by(email = data['email']).all()
            }
            return res
        except Exception:
            return {"Status" : "Insertion Failed , Try to Update if you want to change it"}

          
# Url Configuration
api.add_resource(emails,'/emails')


if __name__ == '__main__':
    app.run(debug=True)