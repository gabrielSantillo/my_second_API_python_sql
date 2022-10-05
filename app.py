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

app.run(debug=True)