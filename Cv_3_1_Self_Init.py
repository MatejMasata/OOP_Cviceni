class MyClass:
    
    def __init__(self, value_for_my_atribute):  # constructor definition, expectation of one parametr to be passed
        self.my_atribute = value_for_my_atribute  # assignment of passed argument into the atribute
        
    def multiply(self, num):
        self.my_atribute = num * self.my_atribute

a=MyClass(1)
b=MyClass(2)

print(a.my_atribute)
print(b.my_atribute)