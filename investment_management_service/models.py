from . import db
from marshmallow_sqlalchemy import ModelSchema


class Investment(db.Model):
    __tablename__ = 'investments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), index=True)
    company_name = db.Column(db.String(80), index=True)
    company_id = db.Column(db.Integer, index=True)
    amount_invested = db.Column(db.DECIMAL(precision=19, scale=4, asdecimal=True))
    percentage_of_fund = db.Column(db.DECIMAL(precision=5, scale=4, asdecimal=True))


class InvestmentSchema(ModelSchema):
    class Meta:
        model = Investment
