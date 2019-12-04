from warrant import Cognito
from flask import request, json, jsonify
from flask import current_app as app

import boto3

user_pool_id = 'us-east-2_55B4TeUfn'
client_id = '7pd4rf1889nh4l91jodo5sdmv7'

client = boto3.client('cognito-idp')

@app.route('/api/pineapple/register', methods=['POST'])
def user_registration():
    cog = Cognito(user_pool_id, client_id)
    email = request.json['email']
    name = request.json['name']
    gender = request.json['gender']
    last_name = request.json['last_name']
    password = request.json['password']
    cog.add_base_attributes(email=email, name=name, gender=gender, family_name=last_name)
    return jsonify(cog.register(email, password))


@app.route('/api/pineapple/confirm_user', methods=['POST'])
def confirm_user():
    email = request.json['email']
    confirmation_code = request.json['confirmation_code']
    cog = Cognito(user_pool_id, client_id)
    return jsonify(cog.confirm_sign_up(confirmation_code=confirmation_code, username=email))


@app.route('/api/pineapple/get_token', methods=['POST'])
def get_token():
    email = request.json['email']
    password = request.json['password']
    cog = Cognito(user_pool_id, client_id, username=email)
    cog.authenticate(password)
    response = {'token': 'Bearer ' + cog.access_token}
    return jsonify(response)


@app.route('/api/pineapple/get_user', methods=['GET'])
def get_user():
    auth_header = request.headers['Authorization']
    bearer, _, token = auth_header.partition(' ')
    if bearer != 'Bearer':
        raise ValueError('Invalid Token')
    else:
        response = client.get_user(AccessToken=token)
    return jsonify(response)

def validate_jwt():

