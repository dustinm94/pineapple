from . import db
from marshmallow_sqlalchemy import ModelSchema


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    company_name =  db.Column(db.String(80), index=True)
    investment_goal = db.Column(db.DECIMAL(asdecimal=True))
    amount_raised = db.Column(db.DECIMAL(asdecimal=True))
    equity_offered = db.Column(db.DECIMAL((1, 2), asdecimal=True))


class CompanySchema(ModelSchema):
    class Meta:
        model = Company
