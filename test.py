import lispapi
import json

eidMap = {'10.1.1.0/24': 'eid-arista',
          '10.1.11.0/24': 'eid-arista',
          '13.1.1.0/24': 'eid-hp'}

rlocMap = {'1.1.1.1': 'arista',
           '1.1.11.1': 'arista',
           '4.4.4.4': 'hp'}

lisp = lispapi.api_init("172.28.171.230", "root", "", 8080, api_debug=True)
siteCache = lisp.get_site_cache()
# print lisp.api_print()
link = []
eids = []
rlocs = []
siteNames = []
for site in siteCache:
    if site['registered'] == 'yes' and site['registered-rlocs']:
        rlocs.append(site['registered-rlocs'][0]['address'])
        siteNames.append(site['site-name'])
        # print eidMap[site['eid-prefix']] \
        #     + "-" + rlocMap[site['registered-rlocs'][0]['address']]
        eid = eidMap[site['eid-prefix']]
        rloc = rlocMap[site['registered-rlocs'][0]['address']]
        link.append({'source': eid, 'target': rloc})
print json.dumps({'link': link}, indent=2)


# print "---EIDS---"
# print eids
# print "---RLOCS---"
# print rlocs
# print siteNames
# print set(rlocs)
