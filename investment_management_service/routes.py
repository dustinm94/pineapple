from flask import request, json, jsonify
from sqlalchemy import exc
from flask import current_app as app
from .equity_calculator import equity_calculator
from .models import db, Investment, InvestmentSchema


@app.route('/api/pineapple/create_investment', methods=['POST'])
def create_investment():
    auth_token = request.headers['Authorization']
    bearer, _, token = auth_token.partition(' ')
    if bearer != 'Bearer':
        raise ValueError('Invalid Access Token')
    else:

        percentage_of_fund = equity_calculator(json.request['amount_invested'],
                                               json.request['size_of_fund'],
                                               json.request['total_equity_offered'])

        new_investment = Investment(user_id=json.request['email'],
                                    company_name=json.request['company_name'],
                                    company_id=json.request['company_id'],
                                    amount_invested=json.request['amount_invested'],
                                    percentage_of_fund=percentage_of_fund)

        db.session.add(new_investment)
        investment_schema = InvestmentSchema()
        try:
            db.session.commit()
            return investment_schema.dump(new_investment), 200
        except exc.SQLAlchemyError as e:
            return jsonify(error=502, text=str(e))


@app.route('/api/pineapple/get_investments', methods=['GET'])
def get_investments():
    investments = Investment.query.all()
    investment_schema = InvestmentSchema(many=True)
    return investment_schema.dumps(investments)


@app.route('/api/pineapple/user_investments/<string:email>', methods=['GET'])
def get_user_investments(email):
    investments = Investment.query.filter(Investment.user_id == email)