from envoy import run
assert run("ssh -T git@gist.github.com").status_code==1
#r=run("ssh -T git@gist.github.com")
print r.status_code # 255
print r.std_out
print r.std_err # ssh_askpass: exec(/usr/libexec/ssh-askpass): No such file or directory
# Host key verification failed.