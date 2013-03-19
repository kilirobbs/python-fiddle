from envoy import run

r=run("git config user.name")
print r.status_code,r.std_out
if r.std_out[-1]=="\n":
    std_out=r.std_out[:-1]
else:
    std_out=r.std_out
print std_out

r=run("git config s.not-existing")
print r.status_code,r.std_out,r.std_err

r=run("git configerr")
print r.status_code,r.std_out,r.std_err

print "----"
try:
    r=run("giterr configerr") # error printed
    if r:
        print r.status_code,r.std_out,r.std_err
    else:
        print "r None"
except Exception,e:
    print "Exception:",str(e)