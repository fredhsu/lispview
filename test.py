# lispview.py
#
# Author: Fred Hsu (fredlhsu@aristacom)
#
# Fetches data from map server and exports it to a file to be consumed
# by d3.json

import lispapi
import json
import time

eidMap = {'10.1.1.0/24': 'eid-arista',
          '10.1.11.0/24': 'eid-arista2',
          '13.1.1.0/24': 'eid-hp',
          '11.1.1.0/24': 'eid-a10',
          '77.7.7.7/32': 'laptop',
          '66.6.6.6/32': 'vm'}

rlocMap = {'1.1.1.1': 'arista',
           '1.1.11.1': 'arista',
           '4.4.4.4': 'hp',
           '2.2.2.2': 'a10'}

while True:
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
    print json.dumps({'link': link}, indent=2)
    time.sleep(2)

# server up web server

# print "---EIDS---"
# print eids
# print "---RLOCS---"
# print rlocs
# print siteNames
# print set(rlocs)
