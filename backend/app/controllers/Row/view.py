from app.classes.row import Row

from flask import jsonify, request

elements = 0
start = 0
end = 0

def create_row(length):
    return [None for i in range(length)]

def add(index, elements):
    return (index + 1 ) % elements

def enqueue(row, item):
    global elements
    global end

    if elements != len(row):
        elements += 1
        end = add(end, elements)
        row[end] = item

def deworming(row):
    global elements
    global start

    if elements != 0:
        removed_item = row[start]
        start = add(start, elements)
        elements -= 1

        return removed_item

@app.endpoint('/create-row')
def index():
    try:
        create_row(10)
    except Exception as error:
        return jsonify({
            "status": False,
            "payload": error.args
        })

