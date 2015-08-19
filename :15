import os
from flask import Flask
from crm import CRM

app = Flask(__name__)

@app.route("/oauth/authorize")
# TODO - GET
def authorize():
    '''
      Request:
        client_id: Your Nylas App ID
        response_type: code
        scope: email
        login_hint: The user’s email address, if available. If no login_hint is present, 
                    Nylas will ask your user for their email address.
        redirect_uri: The web page Nylas should redirect to after sign-in is complete. 
                      Must be one of the Redirect URIs registered with your application in the 
                      Nylas developer console.
        state: (optional) Arbitrary string that is returned as a URL paremeter in your redirect_uri. 
                          You can pass a value here to keep track of a specific user’s authentication flow. 
                          Also may be used to protect against CSRF attacks.

      # Authorization Screen

      Response:
        URL Code: code paramater qry string
    '''
    # TODO - templates

    return "Hello from Python!"

@app.route("/oauth/token")
def hello():
    # TODO - POST
    '''
      Request:
        client_id: Your Nylas App ID
        client_secret: Your Nylas App Secret
        grant_type: authorization_code
        code: The OAuth authorization code you were given in step 3.

      Response:
        access_token: Nylas Access Token
        email_address: Canonicalized email address of the account
        provider: Which provider backs the account, e.g. ‘gmail’ or ‘eas’
        namespace_id: Nylas Namespace ID
        account_id: Nylas Account ID
        error: An error type
        reason: An error message
    '''
    return "Hello from Python!"

@app.route("/accounts")
def hello_1():
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

@app.route("/leads")
def hello_5():
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
def hello_2():
    return "Hello from Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
