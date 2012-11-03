class Person:
    _firstname = None
    _lastname = None

    @property
    def firstname(self):          # firstname = property(firstname)
        """ doc comment for firstname getter """
        return self._firstname

    @firstname.setter             # firstname = firstname.setter(firstname)
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        """ doc comment for lastname getter """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


#i = Person("firstname", "lastname")
i = Person()
i.lastname = 88
print i.lastname