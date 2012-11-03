from plumbum import local
from plumbum.cmd import grep, wc, cat, head

print local.env.user
print local.env.home
print local.env.path
print local.which("python")