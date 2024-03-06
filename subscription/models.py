
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields
from flask_cors import CORS
from flask_restful import Api


# Connection to Supabase Instance by the connection string
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres.ffiwlrevtvzjlszxytpp:PARthib0023!!@aws-0-us-west-1.pooler.supabase.com:5432/postgres'

db = SQLAlchemy(app)
CORS(app,origins=["http://localhost:3000" , "http://localhost:3001"])
api = Api(app)

# Define Your Models Here

class emailModel(db.Model):
    __table__name = 'Emails'
    email = db.Column(db.String, unique=True ,nullable=False)
    
    def __repr__(self) -> str:
        return self.email


with app.app_context():
    db.create_all()


# Marshalling or Serializing Data
# The Fields which will be allowed here , only will be shown in the API

emailSerializer = {
    'email':fields.String,
}


