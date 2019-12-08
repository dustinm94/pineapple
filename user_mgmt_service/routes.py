from flask import request, json, jsonify
from flask import current_app as app

import boto3

user_pool_id = 'us-east-2_55B4TeUfn'
client_id = '7pd4rf1889nh4l91jodo5sdmv7'

client = boto3.client('cognito-idp')


@app.route('/api/pineapple/register', methods=['POST'])
def user_registration():
    email = request.json['email']
    name = request.json['name']
    gender = request.json['gender']
    last_name = request.json['last_name']
    password = request.json['password']
    response = client.sign_up(
        ClientId=client_id,
        Username=email,
        Password=password,
        UserAttributes=[
            {
                'Name': 'name',
                'Value': name,
            },
            {
                'Name': 'family_name',
                'Value': last_name,
            },
            {
                'Name': 'gender',
                'Value': gender
            }
        ]
    )
    return response


@app.route('/api/pineapple/confirm_user', methods=['POST'])
def confirm_user():
    email = request.json['email']
    confirmation_code = request.json['confirmation_code']
    response = client.confirm_sign_up(
        ClientId=client_id,
        Username=email,
        ConfirmationCode=confirmation_code
    )
    return response


@app.route('/api/pineapple/get_token', methods=['POST'])
def get_token():
    email = request.json['email']
    password = request.json['password']
    response = client.initiate_auth(
        ClientId=client_id,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': email,
            'PASSWORD': password
        }

    )
    return response


@app.route('/api/pineapple/get_user', methods=['GET'])
def get_user():
    auth_header = request.headers['Authorization']
    bearer, _, token = auth_header.partition(' ')
    if bearer != 'Bearer':
        raise ValueError('Invalid Token')
    else:
        response = client.get_user(AccessToken=token)
    return jsonify(response)


@app.route('/api/pineapple/logout', methods=['POST'])
def logout():
    id_token = json.request['id_token']
    refresh_token = json.request['refresh_token']
    access_token = json.request['access_token']
    response = client.global_sign_out(
        AccessToken=access_token
    )
    return response


