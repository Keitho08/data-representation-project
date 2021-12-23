import mysql.connector
import requests


db_address = "Keitho08.mysql.pythonanywhere-services.com"
db_username = "Keitho08"
db_password = "PPHtestserver2#"
api_key = "830a9ce1e65ef102a64d03aa6566adc6"

class Customer:
    def __init__(self, id, name, orders, billed, location):
        self.id = id
        self.name = name
        self.billed = billed
        self.orders = orders
        self.location = location
        self.weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key).json()['weather'][0]['description']
    def jsonable(self):
        return self.__dict__


def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(user=db_username,password=db_password,host=db_address,database='Keitho08$customers')
    except mysql.connector.Error as e:
        print(e)
    return conn

def create_customer(conn, customer):
    """
    Create a new project into the projects table
    :param conn:
    :param customer:
    :return: customer id
    """
    sql = ''' INSERT INTO customers (name,orders,billed, location)
              VALUES(%s, %s, %s, %s) '''
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()
    return cur.lastrowid


def select_all_customers(conn):
    """
    Query all rows in the customers table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()
    customers = []
    for row in rows:
        customers.append(Customer(row[0], row[1], row[2], row[3], row[4]).jsonable())
    return customers

def delete_customer(conn, id):
    """
    Delete a customer by customer id
    :param conn:  Connection to the MySQL database
    :param id: id of the customer
    :return:
    """
    sql = 'DELETE FROM customers WHERE id=%s'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def update_customer(conn, customer):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE customers
              SET name = %s,
                billed = %s,
                orders = %s,
                location= %s
              WHERE id = %s'''
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()

def check_user(conn, username, password):
    sql = ''' SELECT count(*) from auth_token where username = %s and password = %s '''
    cur = conn.cursor()
    cur.execute(sql, (username, password))
    result = cur.fetchone()[0]
    if result == 0:
        return False
    else:
        return True