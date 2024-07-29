#!/usr/bin/python3
  2 """
  3 a script that starts a Flask web application
  4 """
  5 
  6 from flask import Flask
  7 app = Flask(__name__)
  8 
  9 
 10 @app.route('/', strict_slashes=False)
 11 def index():
 12     """returns Hello HBNB!"""
 13     return 'Hello HBNB!'
 14 
 15 if __name__ == '__main__':
 16     app.run(host='0.0.0.0', port='5000')
