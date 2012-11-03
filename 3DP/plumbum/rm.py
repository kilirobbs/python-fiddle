from plumbum import local, FG, BG
from plumbum.cmd import rm, echo

(echo["test"] > "./tempfile.txt")()
(rm["./tempfile.txt"])()
(rm["./tempfile_not_existing.txt"] > "/dev/null")()