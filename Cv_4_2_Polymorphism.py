class Person():
    
    def __init__(self, name):
          self.name = name
            
    def personal_introduction(self):
        print(f'My name is {self.name}. I am just a generic person')
         
            
class Teacher(Person):

    def personal_introduction(self):
        print(f'My name is {self.name}. I am a teacher')
    pass
    
    
class Student(Person):
    def personal_introduction(self):
        print(f'My name is {self.name}. I am a student')
    pass

class Worker(Person):
    pass


person = Person('Alice')
person.personal_introduction()

teacher = Teacher('Bob')
teacher.personal_introduction()

student = Student('Carlos')
student.personal_introduction()

worker = Worker('Dereck')
worker.personal_introduction()