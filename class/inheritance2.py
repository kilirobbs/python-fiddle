class Person():
    AnotherName = 'Sue Ann'
    def __init__(self):
        self.FirstName = 'Tom'
        self.LastName = 'Sneed'

    def get_name(self):
        return self.FirstName + ' ' + self.LastName

class Employee(Person):
    def __init__(self):
        self.empnum = 'abc123'

    def get_emp(self):
        print self.AnotherName
        return self.FirstName + ' ' + 'abc'

x = Person()
y = Employee()
print 'start'
print x.get_name()
print y.get_emp()