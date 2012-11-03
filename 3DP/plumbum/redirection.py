from plumbum import local
from plumbum.cmd import grep, wc, cat, head

print ((cat < "basic.py") | head["-n", 4])()

echo 