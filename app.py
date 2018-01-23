"""Flask"""

from flask import Flask, render_template
from models import *
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('test.html')

@app.route("/index")
def index():
    """Home route handler"""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Comments</title>
    </head>

    <body>
        <h>Welcome!</h>
    </body>

    </html>
    """

    return page

@app.route("/comments")
def comments():
    """comments route handler"""
    dict = {}
    for i in COMMENTS:
        dict[i.text] = {i.date}
        
    return render_template('comments.html', comms = dict)

@app.route("/api/v1.0/comments")
def api_comments():
    """JSON comments route handler"""
    jsstring = ''
    for i in COMMENTS:
         jsstring += str(json.dumps(i.__dict__))
    return jsstring
    