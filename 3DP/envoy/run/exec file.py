from envoy import run

f="/Users/nordmenss/.url2sh/https___gist_github_com_raw_80b43df6fc71be4cb545"

r=run(f)
print r
print r.status_code