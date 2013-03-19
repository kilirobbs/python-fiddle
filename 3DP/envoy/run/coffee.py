from envoy import run
f="/Users/nordmenss/git/FIDDLE/coffee-script-fiddle/test.coffee"
cmd="/usr/local/bin/coffee %s" % f
print cmd
r=run(cmd)
print r,r.status_code,r.std_out