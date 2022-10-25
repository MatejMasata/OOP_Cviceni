# Parent class
class ParentClass:
    my_atribute = 5
        
    def my_method(self):
        print(f'Method of a class {self.__class__}')

parent=ParentClass()
parent.my_method()

# Child class, empty implementation
class ChildClass(ParentClass):
    pass

child=ChildClass()
child.my_method()
