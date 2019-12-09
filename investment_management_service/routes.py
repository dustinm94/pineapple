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

        percentage_of_fund = equity_calculator(request.json['amount_invested'],
                                               request.json['size_of_fund'],
                                               request.json['total_equity_offered'])

        new_investment = Investment(user_id=request.json['email'],
                                    company_name=request.json['company_name'],
                                    company_id=request.json['company_id'],
                                    amount_invested=request.json['amount_invested'],
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
    investment_schema = InvestmentSchema()
    return investment_schema.dumps(investments)


@app.route('/api/pineapple/user_investments/health', methods=['GET'])
def endpoint_health_check():
    return 'ping'
