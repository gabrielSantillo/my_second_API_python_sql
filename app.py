from flask import Flask, request
from dbhelpers import run_statement
import json

app = Flask(__name__)

@app.get('/api/item')
def get_all_items():
    results = run_statement("CALL get_all_items()")
    if(type(results) == list):
        items_json = json.dumps(results, default=str)
        return items_json
    else:
        return "Sorry, something has gone wrong."

@app.post('/api/item')
def insert_item():
    item_name = request.json.get('item_name')
    item_descprition = request.json.get('item_descprition')
    item_stock = request.json.get('item_stock')
    results = run_statement("CALL insert_item(?,?,?)", [item_name, item_descprition, item_stock])
    if(type(results) == list):
        id_item_json = json.dumps(results, default=str)
        return id_item_json
    else:
        return "Sorry, something has gone wrong."

@app.patch('/api/item')
def update_item_stock():
    item_id = request.json.get('item_id')
    item_stock = request.json.get('item_stock')
    results = run_statement("CALL update_stock_by_item_id(?,?)", [item_id, item_stock])
    if(type(results) == list):
        id_stock_json = json.dumps(results, default=str)
        return id_stock_json
    else:
        return "Sorry, something has gone wrong."

@app.delete('/api/item')
def delete_item():
    item_id = request.json.get('item_id')
    results = run_statement("CALL delete_item_by_id(?)", [item_id])
    if(type(results) != list):
        return "Item deleted."
    else:
        return "Sorry, something has gone wrong."

app.run(debug=True)