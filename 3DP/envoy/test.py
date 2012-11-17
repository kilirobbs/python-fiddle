from envoy import run

r = run('git config', data='data to pipe in', timeout=2)
r = run('ls')
print r.status_code
print r.std_out
print r.std_err
print r.command