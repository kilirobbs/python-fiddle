from plumbum import local
from plumbum.cmd import grep, wc, cat, head
ls = local["ls"]
chain = ls["-a"] | grep["-v", "\\.py"] | wc["-l"]
print chain
# /bin/ls -a | /usr/bin/grep -v '\.py' | /usr/bin/wc -l

ca