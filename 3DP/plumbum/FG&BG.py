from plumbum import local, FG, BG
from plumbum.cmd import ls, grep

(ls["-a"] | grep["\\.py"]) & FG   

(ls["-a"] | grep["\\.py"]) & BG 