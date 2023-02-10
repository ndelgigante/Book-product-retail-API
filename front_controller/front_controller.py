# import the flask module.  Make sure it is installed in your env!
# The Flask (capital F) class will construct our server for us
from flask import Flask, request, jsonify
from service_layer import user_login
# creating an instance of the Flask class will be our server
app = Flask(__name__)

# This is an in-memory collection to hold objects.
# In an actual implementation, this will call a database to persist data
# Changing this behavior is the focus of this project!
employees = []

# This is a simple boolean that will determine if the user is logged in
# For this project, you don't need to do anything more complicated than this!
logged_in = False

# The server instance can decorate a function
# When the url passed to .route() is called, Flask will execute the function
# A Flask route must return a value, either text, HTML or JSON
@app.route("/")
def index():
    return "Welcome to the employee service!"

# This route will handle the login
@app.route("/login")
def login():
	
	# The global logged_in variable is a simple way to handle logged in status
    global logged_in
	
	# Parsing the login request to retrieve the username and password
    username = request.json["username"]
    password = request.json["password"]
	
	# I have hardcoded the username and password here.  See if you can search user profiles for this step!
    if user_login.login(username, password):
        logged_in = True
        return "You are logged in!"
    else:
        return "Incorrect Username or Password"

@app.route("/logout")
def login():
	# if the user is logged in, this logs them out
    global logged_in
	if logged_in: 
		loggedin = False
		return "Logged out!"
	else:
		return "login first at /login"

# Flask methods should be organized by URL
# In this case, both adding employees and getting all employees is defined on /employees
@app.route("/employees", methods=["GET", "POST"])
def handle_create_read(): 

    # This statement will immediately end the function if the user is not logged in
    if not logged_in: return "please login at /login"
    
    # The request object contains the information sent to the server from the client request
    # By switching behavior on the HTTP method, multiple request types can be handled.
    if request.method == "GET":
        # The get method wants to READ all employees, so we return a json object of the employees
        return jsonify(employees)
    elif request.method == "POST":
        # A post method contain a request body, and the new employee's information is stored there.
        employees.append(request.json)
        # The behavior on a successful ADD is optional, in this case, I am returning all employees, which incudes the new one
        return jsonify(employees)

# Adding an <id> parameter of a URL will be call this function
# This function will handle Updating employees, Deleting employees, and retrieving one employee by their id
@app.route("/employees/<id>", methods=["GET", "PUT", "DELETE"])
def handle_update_delete(id): 

    # This statement will immediately end the function if the user is not logged in
    if not logged_in: return "please login at /login"

    # The GET method at this URL will return one employee if their id matches the value passed in the url 
    if request.method == "GET":
        # I am using a List Comprehension to filter the employees list, then return that employee
        employee = [employee for employee in employees if employee["id"] == id]
        return jsonify(employee)
    # The PUT method will replace an employee in the list if their id matches what was passed
    elif request.method == "PUT":
        # PUT requests also have a method body, in this case it is the employee to be updated
        # Here, I am creating a loop to find the employee by the id from the url. 
        # Can you make this more efficient?
        new_employee = request.json
        index = -1
        for i, employee in enumerate(employees):
            if employee["id"] == id:
                index = i
        if index != -1: employees[i] = new_employee[0]
        return jsonify(employees)
    # The DELETE method will remove an employee in the list if their id matches what was passed
    elif request.method == "DELETE":
        # I am using a List Comprehension to filter the employees list, then return all employees that do NOT match!
        employee = [employee for employee in employees if not employee["id"] == id]
        return jsonify(employee)


# When this python file is run directly, the app will start
if __name__ == "__main__":
    # the port argument changes the port from the default 5000 to a port of your choice
    # the debug argument will, among other things, automatically restart the server when changes are made to code
    app.run(port = 8080, debug = True)