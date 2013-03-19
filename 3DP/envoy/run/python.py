from envoy import run

cmd="python -c 'import sys; print sys.version_info[0]'"
try:
    r=run(cmd)
    print r.status_code,r.std_err
except:
    pass


#r=run("python","import sys; print sys.version_info[0]")
#print r.status_code,r.std_out,r.std_err

cmd="python /Users/nordmenss/git/setuppy/setup.py --fullname"
#print run(cmd)
print run(cmd)
#print r.status_code,r.std_err,r.std_out