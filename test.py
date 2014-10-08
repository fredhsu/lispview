import lispapi

lisp = lispapi.api_init("172.28.171.230", "root", "", 8080, api_debug=True)
siteCache = lisp.get_site_cache()
# print lisp.api_print()
eids = []
rlocs = []
siteNames = []
for site in siteCache:
    print
    print site
    print site['eid-prefix']
    eids.append(site['eid-prefix'])
    if site['registered'] == 'yes' and site['registered-rlocs']:
        rlocs.append(site['registered-rlocs'][0]['address'])
        siteNames.append(site['site-name'])

print "---EIDS---"
print eids
print "---RLOCS---"
print rlocs
print siteNames
# print set(rlocs)
