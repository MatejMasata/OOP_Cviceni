class Person():
    
    def __init__(self, name,age):
          self.name = name
          self.age=age
            
class Student(Person):
    
    current_courses = []  # set default courses for every student

    def __init__(self, name,age,courses):
        super().__init__(name,age)                                  # !! init rodicovske metody
        self.current_courses=courses
        
    def print_courses(self): # method for printing out student courses
        print(f'Student {self.name}\'s courses:')
        for course in self.current_courses:
            print(course)

student=Student("Alice",22,["OOP","Maths"])
student.print_courses()

