class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 
    def get_full_name(self):
        full_name = self.firstname + ' '+  self.lastname
        return full_name

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject 
    def printNameSubject(self):
        print(self.firstname+ ' ' + self.lastname + ', '+ self.subject)


class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def printNameCourse(self):
        print(self.firstname+ ' ' + self.lastname + ', '+ self.course)







