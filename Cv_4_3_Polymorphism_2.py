class Person():
    
    def __init__(self, name):
          self.name = name
            
    def personal_introduction(self):
        #print(f'My name is {self.name}. I am just generic person')
        raise NotImplementedError("This method is abstract")
         
            
class Teacher(Person):
    def personal_introduction(self):
        print(f'My name is {self.name}. I am teacher')
    
    
class Student(Person):
    def personal_introduction(self):
        print(f'My name is {self.name}. I am student')
        
        
        
class MasterStudent(Student):
    def personal_introduction(self):
        print(f'My name is {self.name}. I am master student')
        
        
class Stranger(Person):  
    # stranger doesn't override parent's method with own implementation so he will use implementation of Person (parent class)
    def personal_introduction(self):
        print(f'My name is {self.name}. I am stranger')
    pass

        
# Teacher, Student, MasterStudent overrides parent method with own implementation    
teacher = Teacher('Alice')
student1 = Student('Bob')
student2 = MasterStudent('Carlos')
# Stranger uses parent's implementation, no override
stranger = Stranger('Derek')  
school_register = [teacher, student1, student2, stranger]

for person in school_register:
    person.personal_introduction()