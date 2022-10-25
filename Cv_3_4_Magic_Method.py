class Example:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):
        return f'Example(a={self.a}, b={self.b})'
    
    
example = Example(1,2)
print(example)