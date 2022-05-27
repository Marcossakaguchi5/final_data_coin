from distutils.log import debug
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests
import json
import mongo
from mongo import valor   

app = Flask(__name__)
CORS(app)

@app.route('/')
def inicial():
    return render_template("home.html", resp=valor)   

@app.route('/getCotacao')
def getDados():

    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/find"
    payload = json.dumps({
        "collection": "preco",
        "database": "teste",
        "dataSource": "Cluster0",
        "projection": {
            "_id": 0
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    final_data = json.loads(response.text)

    return jsonify(final_data), 200
    
@app.route('/getHoras')
def getHoras():
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/find"
    payload = json.dumps({
        "collection": "tempo",
        "database": "teste",
        "dataSource": "Cluster0",
        "projection": {
            "_id": 0
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    final_data = json.loads(response.text)

    return jsonify(final_data), 200

app.run(debug=True)