# encoding: utf-8
import json
from db import db as db
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)
conn = None
customers = []

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    conn = db.create_connection()
    if (db.check_user(conn, username, password)):
        return redirect('/customers_home')
    else:
        return render_template('login.html', message="Username or password not correct. Please try again.")

@app.route('/customers_home')
def customers_home():
    return render_template('customers.html', customers=customers)

@app.route('/customers', methods=['GET'])
def get():
    conn = db.create_connection()
    customers = json.dumps(db.select_all_customers(conn))
    conn = None
    return customers

@app.route('/customers', methods=['POST'])
def post():
    name = request.form.get("name")
    billed = request.form.get("billed")
    orders = request.form.get("orders")
    location = request.form.get("location")
    conn = db.create_connection()
    db.create_customer(conn, (name, orders, billed, location))
    conn = None
    return get()

@app.route('/customers', methods=['PUT'])
def put():
    id = request.form.get("id")
    name = request.form.get("name")
    billed = request.form.get("billed")
    orders = request.form.get("orders")
    location = request.form.get("location")
    conn = db.create_connection()
    db.update_customer(conn, (name, orders, billed,location, id))
    conn = None
    return get()

@app.route('/customers/<id>', methods=['DELETE'])
def delete(id=-1):
    conn = db.create_connection()
    db.delete_customer(conn, id)
    conn = None
    return get()

if __name__ == '__main__':

    app.run(debug=True, port=5000, host="0.0.0.0")
