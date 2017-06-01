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
def main():
    tmdb.API_KEY = 'ea8b8b13173cd8da69ef4a48377c6734'
    search = tmdb.Search()
    response = search.movie(query='The Bourne')
    for s in search.results:
        print(s['title'], s['id'], s['release_date'], s['popularity'])

    return s
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
