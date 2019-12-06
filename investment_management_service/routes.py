from flask import request
from sqlalchemy import exc
from flask import current_app as app


@app.route('/api/pineapple/create_company', methods=['POST'])
def create_company():
    x = 1
    # TODO ADD FOUNDER USER