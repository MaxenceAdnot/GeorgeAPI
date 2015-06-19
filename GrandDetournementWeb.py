import socket
from flask import Flask
from GrandDetournementApi import GrandDetournementApi

app = Flask(__name__)

@app.route("/")
def Index():
    gdapi = GrandDetournementApi()
    return gdapi.returnQuote() + '<br />'*4 + 'Running on: ' + socket.gethostname() 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
