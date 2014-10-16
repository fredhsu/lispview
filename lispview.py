# lispview.py
#
# Author: Fred Hsu (fredlhsu@aristacom)
#
# Fetches data from map server and exports it to a file to be consumed
# by d3.json

import lispapi
import json
import time
import flask
from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/lispview/")
def lispview():
    data = fetch()
    return data


eidMap = {'10.1.1.0/24': 'eid-arista',
          '10.1.11.0/24': 'eid-arista2',
          '13.1.1.0/24': 'eid-hp',
          '11.1.1.0/24': 'eid-a10',
          '77.7.7.7/32': '4',
          '66.6.6.6/32': '5'}

rlocMap = {'1.1.1.1': '0',
           '1.1.11.1': '9',
           '4.4.4.4': '1',
           '2.2.2.2': '3',
           '3.3.3.3': '2'}

def fetch():
    lisp = lispapi.api_init("172.28.171.230", "root", "", 8080, api_debug=False)
    siteCache = lisp.get_site_cache()
    # print lisp.api_print()
    link = []
    eids = []
    for site in siteCache:
        if site['registered'] == 'yes' and site['registered-rlocs']:
            eid = eidMap[site['eid-prefix']]
            rloc = rlocMap[site['registered-rlocs'][0]['address']]
            if not eid.startswith("eid"):
                link.append({'source': eid, 'target': rloc})
    return flask.jsonify({'link': link})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
