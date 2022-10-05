# importing librearies to use when making the db connection and building the API
from flask import Flask, request
from dbhelpers import run_statement
import json

# calling the Flask function which will return a value that I will be used for my API
app = Flask(__name__)

# making a get request with the /api/item endpoint
@app.get('/api/item')
# function that will call the procedure responsible to send back all items
def get_all_items():
    # calling the procedure
    results = run_statement("CALL get_all_items()")
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) == list):
        items_json = json.dumps(results, default=str)
        return items_json
    else:
        return "Sorry, something has gone wrong."

# making a get request with the /api/item endpoint
@app.post('/api/item')
# function that will call the procedure responsible to insert an item
def insert_item():
    # grabbing all data needed to insert an item
    item_name = request.json.get('item_name')
    item_descprition = request.json.get('item_descprition')
    item_stock = request.json.get('item_stock')
    # calling the procedure responsible to insert an item
    results = run_statement("CALL insert_item(?,?,?)", [item_name, item_descprition, item_stock])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) == list):
        id_item_json = json.dumps(results, default=str)
        return id_item_json
    else:
        return "Sorry, something has gone wrong."

# making a patch request with the /api/item endpoint
@app.patch('/api/item')
# function that will update the stock of an item
def update_item_stock():
    # grabbing all data needed to update the stock item
    item_id = request.json.get('item_id')
    item_stock = request.json.get('item_stock')
    # calling the procedure responsible to update the stock
    results = run_statement("CALL update_stock_by_item_id(?,?)", [item_id, item_stock])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) == list):
        id_stock_json = json.dumps(results, default=str)
        return id_stock_json
    else:
        return "Sorry, something has gone wrong."

# making a delete request with the /api/item endpoint
@app.delete('/api/item')
# function that will delete an item
def delete_item():
    # grabbing the data needed to delete an item
    item_id = request.json.get('item_id')
    # calling the procedure that will delete an item
    results = run_statement("CALL delete_item_by_id(?)", [item_id])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) != list):
        return "Item deleted."
    else:
        return "Sorry, something has gone wrong."

# making a get request with the /api/employee endpoint
@app.get('/api/employee')
# function that will get an employee based on its id
def get_employee_by_id():
    # grabbing the data needed to get the employee
    employee_id = request.args.get('employee_id')
    # calling the prcedure responsible to get the employee
    results = run_statement("CALL get_employee_by_id(?)", [employee_id])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) == list):
        employee_json = json.dumps(results, default=str)
        return employee_json
    else:
        return "Sorry, something has gone wrong."

# making a post request with the /api/employee endpoint
@app.post('/api/employee')
# function that will insert an employee
def insert_employee():
    # grabbing all data needed to insert an employee
    employee_name = request.json.get('employee_name')
    employee_position = request.json.get('employee_position')
    employee_hourly_wage = request.json.get('employee_hourly_wage')
    # calling the procedure that will insert an employee
    results = run_statement("CALL insert_employee(?,?,?)", [employee_name, employee_position, employee_hourly_wage])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) == list):
        employee_json = json.dumps(results, default=str)
        return employee_json
    else:
        return "Sorry, something has gone wrong."

# making a patch request with the /api/employee endpoint
@app.patch('/api/employee')
# function that will update the hourly wage based on an employee id
def update_hourly_wage():
    # grabbing all data needed to update the hourly wage
    employee_id = request.json.get('employee_id')
    employee_hourly_wage = request.json.get('employee_hourly_wage')
    # calling the procedure that will update the hourly wage
    results = run_statement("CALL update_hourly_wage(?,?)", [employee_id, employee_hourly_wage])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) == list):
        employee_hourly_wage_json = json.dumps(results, default=str)
        return employee_hourly_wage_json
    else:
        return "Sorry, something has gone wrong."

# making a delete request with the /api/employee endpoint
@app.delete('/api/employee')
# caling the function that will delete an employee based on its id
def delete_employee():
    # grabbing the data needed to delete an employee
    employee_id = request.json.get('employee_id')
    # calling the procedure that will delete an employee
    results = run_statement("CALL delete_employee_by_id(?)", [employee_id])
    # checking to see if the response is a list and if yes, turn this response into a JSON, if not, sent back a message
    if(type(results) != list):
        return "Employee deleted."
    else:
        return "Sorry, something has gone wrong."

# starting our application flask server with debug mode turned on
app.run(debug=True)