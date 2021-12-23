# Computer Science and Data Analytic's
## Data Representation
## Assignment 2021
### By: Keith Brazill - G00387845

*This assignement is submitted as part of the requirements for partial fullfilment of a postgraduate diploma in Computer Science with Data Analytics at Galway Mayo Institute of Technology.*

![alt text.](https://learnonline.gmit.ie/pluginfile.php/1/theme_adaptable/logo/1606983803/Transparent%20new.png "GMIT Logo")

# 2. The Project Brief

*Write a program that demonstrates that you understand creating and consuming
RESTful APIs. I will allow a lot of flexibility in this project, so that you can use it as an
opportunity to do something that is useful for your work.*

*Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data.*

# Context
This example code is a basic Python/Flask application for demonstrating how to create and consume Rest APIs. The use case is a CRM (customer relationship management) application, so we are going to create, read, update, delete customers records. 

The application is made up of the following files:

flaskapiexample/
- db/ #folder containing the database
- db/customers.db #the sqlite database
- db/db.py #the module containing the database access functions
- static/css #folder containing the stylesheet
- templates/
- app.py #the flask application, with the "customers" rest apis definition

# Python
In technical terms, Python is an object-oriented, high-level programming language with integrated dynamic semantics primarily for web and app development. It is extremely attractive in the field of Rapid Application Development because it offers dynamic typing and dynamic binding options. 
 
Python is relatively simple, so it’s easy to learn since it requires a unique syntax that focuses on readability. Developers can read and translate Python code much easier than other languages. In turn, this reduces the cost of program maintenance and development because it allows teams to work collaboratively without significant language and experience barriers.
 
Additionally, Python supports the use of modules and packages, which means that programs can be designed in a modular style and code can be reused across a variety of projects. Once you’ve developed a module or package you need, it can be scaled for use in other projects, and it’s easy to import or export these modules.
 
One of the most promising benefits of Python is that both the standard library and the interpreter are available free of charge, in both binary and source form. There is no exclusivity either, as Python and all the necessary tools are available on all major platforms. Therefore, it is an enticing option for developers who don’t want to worry about paying high development costs.

# What is Flask
Flask is a web framework, it’s a Python module that lets you develop web applications easily. 

A Web Application Framework or a simply a Web Framework represents a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management, and so on.

Flask is a web application framework written in Python. It was developed by Armin Ronacher, who led a team of international Python enthusiasts called Poocco. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine.Both are Pocco projects
## WSGI
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web application development. WSGI is the specification of a common interface between web servers and web applications.

## Werkzeug
Werkzeug is a WSGI toolkit that implements requests, response objects, and utility functions. This enables a web frame to be built on it. The Flask framework uses Werkzeg as one of its bases.

## jinja2
jinja2 is a popular template engine for Python.A web template system combines a template with a specific data source to render a dynamic web page.

# What is MySQL
MySQL is an open source relational database management system (RDBMS) with a client-server model. RDBMS is a software or service used to create and manage databases based on a relational model

# What is Javascript
JavaScript is a scripting language used to create and control dynamic website content, i.e. anything that moves, refreshes, or otherwise changes on your screen without requiring you to manually reload a web page.

# What is AJAX
AJAX stands for Asynchronous JavaScript and XML. AJAX is a new technique for creating better, faster, and more interactive web applications with the help of XML, HTML, CSS, and Java Script.
Conventional web applications transmit information to and from the sever using synchronous requests. It means you fill out a form, hit submit, and get directed to a new page with new information from the server.
With AJAX, when you hit submit, JavaScript will make a request to the server, interpret the results, and update the current screen. In the purest sense, the user would never know that anything was even transmitted to the server.
XML is commonly used as the format for receiving server data, although any format, including plain text, can be used, but for rest APIs JSON is the preferred choice.
AJAX is a web browser technology independent of web server software. A user can continue to use the application while the client program requests information from the server in the background.

# What is JQuery
jQuery is a lightweight, "write less, do more", JavaScript library.
The purpose of jQuery is to make it much easier to use JavaScript on your website.
jQuery takes a lot of common tasks that require many lines of JavaScript code to accomplish, and wraps them into methods that you can call with a single line of code.
jQuery also simplifies a lot of the complicated things from JavaScript, like AJAX calls and DOM manipulation.

The jQuery library contains the following features:
- HTML/DOM manipulation
- CSS manipulation
- HTML event methods
- Effects and animations
- AJAX
- Utilities

# What is RestAPI
API is a hypothetical contract between two softwares. Web APIs have made it easy for cross-language applications to work well.
Application Programming Interfaces are commonly used to retrieve data from remote websites. To make a request to a remote web server and retrieve data, we make use of the URL endpoint from where the API is being served. Each URL is called a request and the data that is sent back is called a response.
A RESTful API is an application program interface that uses HTTP requests to GET, PUT, POST and DELETE data. REST based interactions use constraints that are familiar to anyone well known with HTTP. And the interactions communicate their status using standard HTTP status codes.

# What is PythonAnywhere
PythonAnywhere.com is a python hosting platform. It has all the basic Python tools for developing the different use cases (console applications, websites, restAPIs, and so on) . It has a free basic plan. 

# The flask api example application explained
## Application environment
The hosting webserver OS is Windows 2008 R2.  
The application is built with Python 3.8. In order to install Python, download the windows installer from https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe and follow the standard installation process. Setup the Python base folder (usually at C:\Users\<Username>\AppData\Local\Programs\Python\Python38-32) in the PATH environment variable. 
Then, install pip ( the python package manager) that will help to install the Flask module. In order to install pip, download the file at https://bootstrap.pypa.io/get-pip.py, place it in the python base folder then run the command ```python get-pip.py```. 
Finally install Flask module. In order to do so, run the command ```pip install Flask```
The application is simply a crud application for managing the customers data ( name, billed, orders attributes)

## database
The customers database, named Keitho08$customers is located on pythonanywhere.com site. 
it has two tables
- customers, to store customer details with the following fields
-- id, the primary key
-- name 
-- orders
-- billed 
-- location

- auth_token, to store user data with the following fields
-- id 
-- auth_token
-- username
-- password

## app.py
This file is the start up file for the flask rest api application. 

### Import section
The import section contains the referenced files/modules to be used to build our application. 

```import json```
This package will help us to send/receive json content to/from the client (web page)

```from db import db as db```
This is the reference to the file used to interact with the database

```from flask import Flask, render_template, request, jsonify```
These are the references to Flask components. Flask is the class that represents the application. render_template is the class that allows to send to the requester an html responses based on a template. request is the class that allows to manage the request data. jsonify is the class that allows to send the requester a JSON response

### Global variable initialisation
In this section the variables referenced and managed overall the application will be defined

```app = Flask(__name__)```
The Flask web application. 

```conn = None ```
The database connection. It is initialised with the None value

```customers = []``` 
The customers collection

### Login implementation section
```
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')
```
Here we define what is the action to be performed when we call the default route (domain.com"/"). In this case the response is serving the jinja2 template "login.html". jinja2 looks for the template in the default directory "/templates". 
the route /login linked to the POST method will handle the server call performed when the submit button on the login.html page is clicked. 

```
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    conn = db.create_connection()
    if (db.check_user(conn, username, password)):
        return redirect('/customers_home')
    else:
        return render_template('login.html', message="Username or password not correct. Please try again.")
```
The function will check for a user with the credentials passed as input into the auth_token table. in case the check_user function of the db module returns true, the /customers_home route is called. on the other end , in case it fails, the login page is shown, with an error message. 

The customers_home route will show the customers.html template
```
@app.route('/customers_home')
def customers_home():
    return render_template('customers.html', customers=customers)
```

### APIs implementation section
APIs are functions that respond to a web request. Web requests are defined by a route (the part of the url after the "domain.com/"), an HTTP method and parameters

#### customers - GET
```
@app.route('/customers', methods=['GET'])
def get():
    conn = db.create_connection(database)
    customers = json.dumps(db.select_all_customers(conn))
    conn = None
    return customers
```
Here we define what is the action to be performed when the webpage calls the route (domain.com"/customers" with the GET method). 
This is the first API we define. The GET method returns the json list of all the customers defined in the database. 
First thing to do is to create a connection to the database. in order to do so, we use an helper function from the db.py module
```conn = db.create_connection(database)```
Then, once we get the connection, we can query the database. As before, we use an helper function from the db.py module. the db.select_all_customers function retrieves a list of customers from the database. we will explain better the details of this function in the db.py section
```customers = json.dumps(db.select_all_customers(conn))```
the result of the query is then formatted in json. the formatting is performed using the helper function dumps from json module[8]
before returning the result to the webpage, we do some clean up with 
```conn = None```
then we return the result
```return customers```

#### customers - POST
Customers POST route will handle the insertion of a new record into the customers table
```
@app.route('/customers', methods=['POST'])
def post():
```

in the first section the data from the body of the request will be taken and mapped to local variable
```
    name = request.form.get("name")
    billed = request.form.get("billed")
    orders = request.form.get("orders")
    location = request.form.get("location")
```
then the db module function "create_customer" is called passing the parameters
```
conn = db.create_connection()
db.create_customer(conn, (name, orders, billed, location))
```
in the end, the result of the get function (in order to send the refreshed list of customers) is called
```
return get()
```
#### customers - PUT
Customers PUT route will handle the update of an existing record of the customers table
```
@app.route('/customers', methods=['PUT'])
def put():
```
in the first section the data from the body of the request will be taken and mapped to local variable
```
    id = request.form.get("id")
    name = request.form.get("name")
    billed = request.form.get("billed")
    orders = request.form.get("orders")
    location = request.form.get("location")
```
then the db module function "update_customer" is called passing the parameters
```
conn = db.create_connection()
db.update_customer(conn, (name, orders, billed, location, id))
```
in the end, the result of the get function (in order to send the refreshed list of customers) is called
```
return get()
```
#### customers - DELETE
Customers DELETE route will handle the deletion of a record from the customers table
```
@app.route('/customers/<id>', methods=['DELETE'])
def delete(id=-1):
```
please note that the value following the /customers/ will be automatically mapped as the id input parameter. in case nothing is sent as parameter, then the default value -1 is used. 
then the db module function "delete_customer" is called passing the parameters
```
conn = db.create_connection()
db.delete_customer(conn, id)
```
in the end, the result of the get function (in order to send the refreshed list of customers) is called
```
return get()
```
## db.py
This is the file containing the instructions for creating and updating the database and the records inside

### Import section
The import section contains the referenced files/modules to be used to build our application. 

```import mysql.connector```
This package will help us interact with the database[11]

### Global variable initialisation
In this section the variables referenced and managed overall the application will be defined
in details, we will store as global variables the database connection details to be used and the third party API KEY (https://openweathermap.org/api)
```
db_address = "Keitho08.mysql.pythonanywhere-services.com"
db_username = "Keitho08"
db_password = "PPHtestserver2#"
api_key = "830a9ce1e65ef102a64d03aa6566adc6"
```

### Customer class definition
In order to map out the customers data we will define a Customer class. A Class is like an object constructor, or a "blueprint" for creating objects.
the first command 
```class Customer:```
starts the definition of a class

then we define the constructor method, named __init__
```def __init__(self, id, name, orders, billed, location):```
__init__ method has the following input parameters
- self: a reference to the object being created
- id: the customer id, taken from the database
- name: the name of the customer
- orders: the number of orders submitted by the customer
- billed: an information on how much has billed to the customer
- location: the customer's city. 

Following the initialisation of the instance internal variables with the input parameters
```
self.id = id
self.name = name
self.billed = billed
self.orders = orders
self.location = location
```
These variables belong to the instance. 

Following this there is the initialisation of the weather instance variable, by calling the third party api
```
self.weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key).json()['weather'][0]['description']
```
in detail we use the requests.get method for consuming the third party API. we are going to use the current weather api[12]. the input parameters of this api are
- q: the customer location
- appid: the appid provided by the web site. we use the api_key defined as global variable

then we convert the response in json with the method .json of the response object returned by the request.get method
```.json()```

then we retrieve the weather description from the json. 

this is the example response json
```
{
     "coord": {
       "lon": -0.13,
       "lat": 51.51
     },
     "weather": [
       {
         "id": 300,
         "main": "Drizzle",
         "description": "light intensity drizzle",
         "icon": "09d"
       }
     ],
     "base": "stations",
     "main": {
       "temp": 280.32,
       "pressure": 1012,
       "humidity": 81,
       "temp_min": 279.15,
       "temp_max": 281.15
     },
     "visibility": 10000,
     "wind": {
       "speed": 4.1,
       "deg": 80
     },
     "clouds": {
       "all": 90
     },
     "dt": 1485789600,
     "sys": {
       "type": 1,
       "id": 5091,
       "message": 0.0103,
       "country": "GB",
       "sunrise": 1485762037,
       "sunset": 1485794875
     },
     "id": 2643743,
     "name": "London",
     "cod": 200
     }

```

Then in order to retrieve the data of interest we use 
```['weather'][0]['description']```

Finally we define method for making the Class serializable as JSON Object and send it back as an api response
```
def jsonable(self):
        return self.__dict__
```
the command 
```
return self.__dict__
```
returns a dictionary (name:value list) of the instance variables.

Then follow the method for interacting with the database

### Create connection
```
def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(user=db_username,password=db_password,host=db_address,database='Keitho08$customers')
    except mysql.connector.Error as e:
        print(e)
    return conn
```
create_connection method creates a connection to the database, using the global variables as db host, username, password and database name to connect.
conn = mysql.connector.connect(user=db_username,password=db_password,host=db_address,database='Keitho08$customers')

try..except construct handles possible errors in operations enclosed (missing db connection link or wrong username/password)

it returns the connection reference to be used for subsequent operations

### Create customer
```
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
```
this method is used for creating a new customer record

in detail it takes the following parameters
- conn: a reference to an active connection
- customer: an array with the customer info

then we define the sql command to be used for creating a customer record into the customers table
```
sql = ''' INSERT INTO customers (name,orders,billed, location)
              VALUES(%s, %s, %s, %s) '''
```
we use %s as placeholder for the input paramters
the following command is for creating a cursor for sending the database the commands. the cursor is created from the active connection object
```
cur = conn.cursor()
```
then we execute the sql command defined above. the execute method gets as second parameter a list of parameters. it will automatically replace the %s with the paramters, taken with the same order as they are (1st %s will be replaced with the 1st element of the array, 2nd %s with the 2nd element of the array and so on)
```
cur.execute(sql, customer)
```

### Retrieve the list of the customers
in order to retireve  a customer list from the database we define the following method 
```
def select_all_customers(conn):
```
this method takes as input an active connection object 
the following command is for creating a cursor for sending the database the commands. the cursor is created from the active connection object
```
cur = conn.cursor()
```
then we execute the command for retrieving the data
```
cur.execute("SELECT * FROM customers")
```
the execute parameter taked the SQL command to be used

then we retrieve all the records from the database
```
rows = cur.fetchall()
```
then we loop for all the records and create a list of Customer objects. by calling the jsonable method of the Customer object we make sure that we can return this list as response of a rest api call
```
customers = []
for row in rows:
   customers.append(Customer(row[0], row[1], row[2], row[3], row[4]).jsonable())
```
then we return the customers array
```
return customers
```

### Updating a customer record
in order to update a customer we define the following method 
```
def update_customer(conn, customer):
```
this method takes as input an active connection object and the paramters of the customer (as array) record to be updated
then we define the sql command to be used. %s is the parameter the execute method will replace
```
sql = ''' UPDATE customers
              SET name = %s,
                billed = %s,
                orders = %s,
                location= %s
              WHERE id = %s'''
```
the following command is for creating a cursor for sending the database the commands. the cursor is created from the active connection object
```
cur = conn.cursor()
```
then we execute the sql command defined above. the execute method gets as second parameter a list of parameters. it will automatically replace the %s with the paramters, taken with the same order as they are (1st %s will be replaced with the 1st element of the array, 2nd %s with the 2nd element of the array and so on)
```
cur.execute(sql,customer)
```
at the end we call "commit method on the connection" to make the database modification persistent
```
conn.commit()
```

### Deleting a customer record
in order to delete a customer we define the following method 
```
def delete_customer(conn, id):
```
this method takes as input an active connection object and the id of the customer record to be deleted
then we define the sql command to be used. %s is the parameter the execute method will replace
```
sql = 'DELETE FROM customers WHERE id=%s'
```
the following command is for creating a cursor for sending the database the commands. the cursor is created from the active connection object
```
cur = conn.cursor()
```
then we execute the sql command defined above. the execute method gets as second parameter a list of parameters. it will automatically replace the %s with the paramters, taken with the same order as they are (1st %s will be replaced with the 1st element of the array, 2nd %s with the 2nd element of the array and so on)
```
cur.execute(sql, (id,))
```
at the end we call "commit method on the connection" to make the database modification persistent
```
conn.commit()
```
### check user existence
this function of the db module will be used to allow the user to log in to the system
```
def check_user(conn, username, password):
```
this method takes as input an active connection object and the user parameters to be checked
then we define the sql command to be used. %s is the parameter the execute method will replace
```
sql = ''' SELECT count(*) from auth_token where username = %s and password = %s '''
```
the following command is for creating a cursor for sending the database the commands. the cursor is created from the active connection object
```
cur = conn.cursor()
```
then we execute the sql command defined above. the execute method gets as second parameter a list of parameters. it will automatically replace the %s with the paramters, taken with the same order as they are (1st %s will be replaced with the 1st element of the array, 2nd %s with the 2nd element of the array and so on)
```
cur.execute(sql, (username,password))
```
then we check if any record matches the parameters. the sql command will return 1 in case the record exists, 0 otherwise.
```
result = cur.fetchone()[0]
```
in order to return a boolean value we check the result variable and return accordingly
```
    if result == 0:
        return False
    else:
        return True
```
##login.html
this is the page that allows the user to input the credentials and log into the customers management page (customers.html)
it is really basic page, with a form
```
<form action="/login" method="post">
```
where it is defined in the action the url where to send the data. the method attribute tells the browser how to send the data (by using "post" as value, we say the browser to send the data as body of the request instead of appending them to the url)

inside the form tag the two input fields, username and password with their respective labels
```
<label for="fname">Username:</label><br>
<input type="text" id="username" name="username"><br>
<label for="lname">Password:</label><br>
<input type="password" id="password" name="password" ><br><br>
```

finally, also inside the form there is the submit button to submit the form and send the data to the server
```
<input type="submit" value="Submit">
```
##customer.html
this is the html file that contains also the javascript for interacting with flask apis via the AJAX functionalities provided by JQuery

the first section is made up of html standard tags. we define the title of the page as "Customers"
```
<!DOCTYPE html>
<html>
<head>
    <title>Customers</title>
 ```
 then we recall jquery library from the cdn 
 ```
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
 ```
we need to include this library in order to use the JQuery methods


### Javascript function section
enclosed in this tag there are the javascript functions used by the html page 
```
<script type="text/javascript">
```

#### Fill table function
the filltable function is used for creating the customer table
it takes as parameter a list of Customers object
then for each record it creates the html code of a table row where each column has a specific value of the customer object (the first cell is the ID, the second cell with the name, and so on)
the last cell is filled up with two links 
Edit: this link has the javascript function as handler of the onclick event. the onclick event is fired when the link is clicked. the handler method is the Edit function described below
Delete: this link has the javascript function as handler of the onclick event. the onclick event is fired when the link is clicked . the handler method is the Delete function described below

#### Edit function
 the edit function performs the action to be done when the "Edit" link near a customer record is clicked 
 ```
 function edit(id) {
            $('#id').val($('#customer' + id + " td:nth-child(1)").text())
            $('#name').val($('#customer' + id + " td:nth-child(2)").text())
            $('#orders').val($('#customer' + id + " td:nth-child(3)").text())
            $('#billed').val($('#customer' + id + " td:nth-child(4)").text())
            $('#location').val($('#customer' + id + " td:nth-child(5)").text())
        }
```

this function takes one parameter, the id of the customer. 
here we use the JQuery helper method $ for retrieving a reference of the objects, using the css selector. in detail we use $('#id') for retrieving the reference of the input field with 'id' attribute that equals to 'id'
with the val method of the object reference retrieved before, we insert a value in the input field. 
the value to be inserted is taked from the table td nth cell of the row with id "customer<id>" . please note that the id of the customer is also used as record id in the html table created with the filltable() function. 
 
#### Delete function
The del function perform the action to be done when "Delete" link near a customer record is clicked
this function takes one parameter, the id of the customer. 
in detail an ajax call to the customer rest api is performed, using the delete http method
the function uses the JQuery $.ajax helper function to perform the call
```
$.ajax({
                dataType: "json",
                method: "DELETE",
                url: "/customers/" + id,
            }).done(function (data) {
                fillTable(data);
            });
```
as shown, the method here is DELETE ( and it will map the corresponding route of the customers RestAPI ). moreover, the id to be deleted is set right after the "customers/". as the definition of the restapi explains, the text after "the customers/" string will be mapped as input parameter
as the delete rest api returns the new customer list taken from the database, the filltable function is called in order to refresh the UI. 

#### Update function
the update function performs the action of updating one customer data. it will fire when the "Create/Update" is clicked AND the "id" field has a meaningful value (this logic is handled by the "create_update" function)
the update function takes all the data of the user form (populated when on of the "Edit" links on the table is clicked) and sends them to the server via AJAX call. 
in this case, the PUT method is used in order to call the correct function
all the data are passed into the data attribute. that means that will be incorporated in the body of the http request sent to the server
```
            $.ajax({
                dataType: "json",
                method: "PUT",
                url: "/customers",
                data: "id=" + id + "&name=" + name + "&billed=" + billed + "&orders=" + orders + "&location=" + location
            }).done(function (data) {
                fillTable(data);
                clean()
            });
        }
```
as the delete rest api returns the new customer list taken from the database, the filltable function is called in order to refresh the UI. 

# References
[1]https://www.pythonforbeginners.com/learn-python/what-is-python
[2]https://pythonbasics.org/what-is-flask-python/
[3]https://www.w3schools.com/jquery/jquery_intro.asp
[4]https://towardsdatascience.com/restful-apis-in-python-121d3763a0e4
[5]https://www.hostinger.com/tutorials/what-is-mysql
[6]https://help.pythonanywhere.com/pages/
[7]https://flask.palletsprojects.com/en/1.1.x/installation/#:~:text=Install%20Flask%C2%B6%20Within%20the%20activated%20environment%2C%20use%20the,or%20update%20the%20code%20from%20the%20master%20branch%3A
[8]https://www.educba.com/flask-jsonify/
[9]https://tedboy.github.io/flask/generated/generated/flask.Request.html
[10]https://www.programcreek.com/python/example/51521/flask.render_template
[11]https://realpython.com/python-mysql/
[12]https://openweathermap.org/current
[13]https://www.w3schools.com/python/python_classes.asp
[14]https://www.tutorialspoint.com/ajax/what_is_ajax.htm
[15]https://www.w3schools.com/sql/sql_quickref.asp 
[16]https://www.w3schools.com/jquery/jquery_selectors.asp#:~:text=jQuery%20selectors%20allow%20you%20to%20select%20and%20manipulate,in%20addition%2C%20it%20has%20some%20own%20custom%20selectors.
[17]https://vegibit.com/how-to-redirect-to-url-in-python-flask/#:~:text=How%20To%20Redirect%20To%20Url%20In%20Python%20Flask,are%20simply%20returning%20some%20text%20to%20the%20user.
[18]https://support.reallysimplesystems.com/api-v4/
[19] https://www.zoho.com/crm/crm-software.html

