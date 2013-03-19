from github3 import login

gh = login(
    "cancerhermit", 
    "nAotzwlKkxrfbHwrCM+9eGLXYiVMTSGAUkqrqniTTXCYHAMQNxvI6Og=="
)
print gh.list_gists("cancerhermit")