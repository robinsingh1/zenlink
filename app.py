import os
import requests
from flask import Flask
from crm import CRM
from flask import render_template
from flask import request

app = Flask(__name__)
BASE_URL = "https://api.cloud-elements.com/elements/api-v2"

@app.route("/v1/authorize")
# TODO - GET
def authorize():
    #print request
    print "lol", request
    crm = request.args.get('crm')
    print crm
    if crm == "pipedrive":
      return render_template('crm_auth.html', crm_name="PIPEDRIVE")
    elif crm == "salesforce":
      return render_template('crm_auth.html', crm_name="SALESFORCE")
    elif crm == "zohocrm":
      return render_template('crm_auth.html', crm_name="ZOHO CRM")
    elif crm == "closeio":
      return render_template('crm_auth.html', crm_name="CLOSE.IO")
    elif crm == "infusionsoft":
      return render_template('crm_auth.html', crm_name="INFUSIONSOFT")
    return render_template('hello.html')

@app.route("/oauth/token")
def hello():
    # TODO - POST
    return "Hello from Python!"

#TODO - add http auth decorator
@app.route("/v1/crm/<str:endpoint>")
def crm_requests():
    # TODO  -------
    # Translate element_id from zenlink to cloudelement

    if request.method == 'GET':
      req = request.get
    elif request.method == 'PUT':
      req = request.put
    elif request.method == 'DELETE':
      req = request.delete
    elif request.method == 'POST':
      req = request.post

    headers = {'Authorization': 'User N+tJ8a+m0eGK/NVk9dleWkjfvaNF/w5nR2awJWtZ7Ao= Organization 821b4da023c419236686cf087c7d38e6, Element: Acl1dcg3gBjLVb/NF8enpMAatObZSaTICqGOGxyYxTk='}
    r = req(BASE_URL+"/hubs/crm/"+endpoint, 
            headers=headers)
    return r.json()


@app.route("/accounts")
def hello_1():
    # if type post
    ''' '''
    # elif type get
    ''' '''
    ''' '''
    return "Hello from Python!"

@app.route("/bulk/query")
def hello_2():
    return "Hello from Python!"
  
@app.route("/contacts")
def hello_3():
    return "Hello from Python!"

@app.route("/leads")
def hello_4():
    return "Hello from Python!"

@app.route("/objects")
def hello_6():
    return "Hello from Python!"

@app.route("/opportunities")
def hello_7():
    return "Hello from Python!"

@app.route("/ping")
def hello_8():
    return "Hello from Python!"

@app.route("/users")
def hello_9():
    return "Hello from Python!"

@app.route("/{objectName}")
# TODO - objectname
def hello_10():
    return "Hello from Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
