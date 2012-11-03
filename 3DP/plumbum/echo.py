from plumbum import local
from plumbum.cmd import cat, echo

(echo["test"] > "./echo.txt")()

print (cat["./echo.txt"])()