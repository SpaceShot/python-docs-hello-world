import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello WPSD Coders"

replit_token = os.getenv("REPLIT")

if replit_token:
  app.run(host='0.0.0.0', port=8080)
