class volume():
    value = None

    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.value)

v = volume(14)
print v
if v > 0:
    print ">0"
else:
    print "<0"
