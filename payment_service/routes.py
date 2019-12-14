from flask import request, json, jsonify
from flask import current_app as app
from flask_cors import cross_origin
import stripe


stripe.api_key = 'sk_test_j1CvBmbOHBtYSwVpWG8ZnYc100ny492Yzc'


@app.route('/api/pineapple/one_time_payment', methods=['POST'])
@cross_origin()
def one_time_payment():
    amount = request.json['amount']
    name = request.json['name']

    session = stripe.checkout.Session.create(
      payment_method_types=['card'],
      line_items=[{
        'name': name,
        'description': 'investment fund',
        'images': ['https://example.com/t-shirt.png'],
        'amount': amount,
        'currency': 'usd',
        'quantity': 1,
      }],
      success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
      cancel_url='https://example.com/cancel',
    )

    return jsonify(session), 200