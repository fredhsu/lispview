# lispview.py
#
# Author: Fred Hsu (fredlhsu@aristacom)
#
# Fetches data from map server and exports it to a file to be consumed
# by d3.json

import lispapi
import json
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/lispview/")
def lispview():
    return fetch()


eidMap = {'10.1.1.0/24': 'eid-arista',
          '10.1.11.0/24': 'eid-arista',
          '13.1.1.0/24': 'eid-hp'}

rlocMap = {'1.1.1.1': 'arista',
           '1.1.11.1': 'arista',
           '4.4.4.4': 'hp'}

def fetch():
    lisp = lispapi.api_init("172.28.171.230", "root", "", 8080, api_debug=True)
    siteCache = lisp.get_site_cache()
    # print lisp.api_print()
    link = []
    eids = []
    # rlocs = []
    # siteNames = []
    for site in siteCache:
        if site['registered'] == 'yes' and site['registered-rlocs']:
            eid = eidMap[site['eid-prefix']]
            rloc = rlocMap[site['registered-rlocs'][0]['address']]
            # rlocs.append(rloc)
            # siteNames.append(site['site-name'])
            link.append({'source': eid, 'target': rloc})
    # write this to a file
    return json.dumps({'link': link}, indent=2)

if __name__ == "__main__":
    app.run()
