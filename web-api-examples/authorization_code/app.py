import requests
import os
from flask import Flask

client_id = 'c47bbd430f764bffa71d5780f3e41fb0' # Your client id
client_secret = 'd35e0e198aa144f99ebbe7c79da999fc' # Your secret
redirect_uri = 'http://localhost:8888/callback/' # Your redirect uri

stateKey = 'spotify_auth_state'

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'

# if __name__ == '__main__':
#     app.debug = True
#     app.run()