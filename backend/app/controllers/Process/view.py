from app import *

from flask import jsonify, request


@app.endpoint('/teste')
def index():
    try:
        return jsonify({
            "mensagem":"Tchau"
        })
    except Exception as error:
        return jsonify({
            "status":False,
            "payload":error.args
        })

@app.endpoint('/create-process')
def index():
    try:
        content = request.get_json(silent = True)
        processos=[]
        
        for i in content['n_process']:
            processos.append(Process(content['process_time']))
        
        return jsonify({
            "teste": "Tchau"
        })

        
    
    except Exception as error:
        return jsonify({
            "status":False,
            "mensagem": "Problem in create process",
            "payload": error.args
        })