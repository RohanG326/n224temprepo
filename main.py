from flask import render_template, request
from __init__ import app
import requests
def aboutme():
    print("Hi my name is Rohan and Welcome to My Beautiful Dark Twisted Fantasy (Kanye reference)")
    return

if __name__ == "__main__":
    app.run(debug=True, port=8081)