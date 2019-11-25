from flask import Flask, escape, request, jsonify,redirect
import requests
import os,sys

app = Flask(__name__)


@app.route('/')
def hello():
    #redirecionar para o Ip alocado da máquina
    return redirect("", code=302)

key = "endpoint"
server = os.getenv(key)
task = sys.argv[1]
tasks = ["post","get","find","delete","put"]


@app.route('/Tarefa/',methods=['GET'])
def getTasks():
    r = requests.get(server+"Tarefa/")
    return r.json()

@app.route('/Tarefa/',methods=['POST'])
def postTasks():

    name = sys.argv[2]
    description = sys.argv[3]

    data = { 'name':name ,
            'description': description
    }
    r = requests.post(server+"Tarefa/", data = data)
    return r.content

@app.route('/Tarefa/<name>',methods=['GET'])
def getTasksID(name):
    id = sys.argv[2]
    r = requests.get(server+"Tarefa/" + id)
    if(r.status_code == "200"):
        return "" 
    else:
        return "Could't Get"
@app.route('/Tarefa/<name>', methods = ['PUT'])
def updateTask(name):
    id = sys.argv[2]
    
    name = sys.argv[3]
    description = sys.argv[4]

    data = { 'name':name ,
            'description': description
    }
    r = requests.put(server+"Tarefa/" + id,data = data)

    if(r.status_code == "200"):
        return "Updated" 
    else:
        return "Could't Update"

@app.route('/Tarefa/<name>', methods = ['DELETE'])
def deleteTask(name):

    id = sys.argv[2]
    r = requests.delete(server+"Tarefa/" + id)
    if(r.status_code == "200"):
        return "Deleted" 
    else:
        return "Could't Delete"

@app.route('/healthcheck/', methods = ['GET'])
def healthTask():
    return "",200


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

