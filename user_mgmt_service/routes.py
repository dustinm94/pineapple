from warrant import Cognito
from flask import request, json
from flask import current_app as app

user_pool_id = 'us-east-2_55B4TeUfn'
client_id = '7pd4rf1889nh4l91jodo5sdmv7'


@app.route('/api/pineapple/register', methods=['POST'])
def user_registration():
    cog = Cognito(user_pool_id, client_id)
    email = request.json['email']
    name = request.json['name']
    gender = request.json['gender']
    last_name = request.json['last_name']
    password = request.json['password']
    cog.add_base_attributes(email=email, name=name, gender=gender, family_name=last_name)
    cog.register(email, password)
    return cog.register(email, password)