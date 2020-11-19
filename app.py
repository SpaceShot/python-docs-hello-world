import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello WPSD Coders"

@app.route("/page2")
def page2hello():
    return "Hello WPSD Coders from Page 2"

replit_token = os.getenv("REPLIT")

if replit_token:
  app.run(host='0.0.0.0', port=8080)