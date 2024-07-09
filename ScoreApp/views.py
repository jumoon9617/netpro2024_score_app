from flask import Flask,request,jsonify
from ScoreApp import app
from ScoreApp import db

@app.route('/')
def index():
    print('client connected!')
    return 'hello manager!'

@app.route('/sendData', methods=['POST'])
def sendData():
    data = request.json
    score = data.get('score')
    playerName = data.get('playerName')
    
    db.add_data(score, playerName)
    print(jsonify({'score': score, 'playerName': playerName}))

@app.route('/getData', methods=['GET'])
def getData():
    data = db.display_list()
    return data