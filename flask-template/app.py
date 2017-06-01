from flask import Flask, render_template, redirect, url_for
from flask import send_file
from flask import json
from pprint import pprint
#from conduce import conduce


import requests
import tmdbsimple as tmdb


import json

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello Word'
#
# @app.route('/facturas')
# def facturas():
#     pdf = factura()
#     return send_file(pdf)

# @app.route('/conduces')
# def conduces():
#     pdf = conduce()
#     return send_file(pdf)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
