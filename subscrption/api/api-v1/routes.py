# Define entire routes here
# This file is used to define the routes for the API
# The routes are defined using the Flask-RESTPlus library
# The routes are defined in the API class
# The API class is used to define the routes
# The API class is used to define the routes for the API

from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import request
from flask import jsonify
from flask import make_response
from flask import Response
import json
from flask import Blueprint

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Subscription API',
          description='A simple Subscription API',
          )

ns = api.namespace('subscriptions', description='Subscription operations')

subscription = api.model('Subscription', {
    'id': fields.Integer(readonly=True, description='The subscription unique identifier'),
    'name': fields.String(required=True, description='The subscription name'),
    'email': fields.String(required=True, description='The subscription email'),
    'subscribed_on': fields.DateTime(required=True, description='The subscription date'),
})

class SubscriptionDAO(object):
    def __init__(self):
        self.counter = 0
        self.subscriptions = []

    def get(self, id):
        for subscription in self.subscriptions:
            if subscription['id'] == id:
                return subscription
        api.abort(404, "Subscription {} doesn't exist".format(id))

    def create(self, data):
        subscription = data
        subscription['id'] = self.counter = self.counter + 1
        self.subscriptions.append(subscription)
        return subscription

    def update(self, id, data):
        subscription = self.get(id)
        subscription.update(data)
        return subscription

    def delete(self, id):
        subscription = self.get(id)
        self.subscriptions.remove(subscription)

    def get_all(self):
        return self.subscriptions

    def get_all_json(self):
        return jsonify(self.subscriptions)

    def get_all_response(self):
        return make_response(jsonify(self.subscriptions))


DAO = SubscriptionDAO()
DAO.create({'name': 'John', 'email': 'johndoe@email.com', 'subscribed_on': '2019-01-01'})

@ns.route('/')
class SubscriptionList(Resource):
    @ns.doc('list_subscriptions')
    @ns.marshal_list_with(subscription)
    def get(self):
        '''List all subscriptions'''
        return DAO.get_all()

    @ns.doc('create_subscription')
    @ns.expect(subscription)
    @ns.marshal_with(subscription, code=201)
    def post(self):
        '''Create a new subscription'''
        return DAO.create(api.payload), 201

@ns.route('/json')
class SubscriptionListJson(Resource):
    @ns.doc('list_subscriptions_json')
    def get(self):
        '''List all subscriptions'''
        return DAO.get_all_json()

@ns.route('/response')
class SubscriptionListResponse(Resource):
    @ns.doc('list_subscriptions_response')
    def get(self):
        '''List all subscriptions'''
        return DAO.get_all_response()

@ns.route('/<int:id>')
@ns.response(404, 'Subscription not found')
@ns.param('id', 'The subscription identifier')
class Subscription(Resource):
    @ns.doc('get_subscription')
    @ns.marshal_with(subscription)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_subscription')
    @ns.response(204, 'Subscription deleted')
    def delete(self, id):
        '''Delete a subscription given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(subscription)
    @ns.marshal_with(subscription)
    def put(self, id):
        '''Update a subscription given its identifier'''
        return DAO.update(id, api.payload)

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
