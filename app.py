import json
import sqlite3

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def Welcome():
    return 'Welcome - Please refer to README for instructions'


@app.route('/api/company/operators', methods=['GET'])
def api_operators_for_company():
    company = request.args.get('companyName')
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except:
        print("Something went wrong")
    cur = conn.cursor()
    cur.execute("select nm_socio from MainDB where nm_fantasia =?;", [company])
    rows = cur.fetchall()
    return json.dumps(rows)


@app.route('/api/operator/companies', methods=['GET'])
def api_companies_for_operator():
    operator = request.args.get('operatorName')
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except:
        print("Something went wrong")
    cur = conn.cursor()
    cur.execute("select nm_fantasia  from MainDB where nm_socio =?;", [operator])
    rows = cur.fetchall()
    return json.dumps(rows)


@app.route('/api/company/companies', methods=['GET'])
def api_companies_sharedOperators():
    companyOperator = request.args.get('companyOperator')
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except:
        print("Something went wrong")
    cur = conn.cursor()
    cur.execute("select nm_fantasia from MainDB where nm_socio IN (select nm_socio from MainDB where nm_fantasia = ?);",
                [companyOperator])
    rows = cur.fetchall()
    return json.dumps(rows)


if __name__ == '__main__':
    app.run()
