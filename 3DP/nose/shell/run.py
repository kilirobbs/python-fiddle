from envoy import run

print run("which nosetests").std_out
cmd="/usr/local/bin/nosetests --with-coverage --cover-erase --cover-html"
r=run(cmd)
print r

