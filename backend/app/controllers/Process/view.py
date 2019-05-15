from app import *
from app.classes.process.Process import *
from flask import jsonify, request


@app.endpoint('/create-process')
def index():
    try:
        content = request.get_json(silent = True)
        processos=[]
        
        for i in content['n_process']:
            processos.append(Process(content['process_time']))
        
        return processos

        
    
    except Exception as error:
        return jsonify({
            "status":False,
            "mensagem": "Problem in create process",
            "payload": error.args
        })