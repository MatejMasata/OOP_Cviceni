class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        
d = Dog('Fido')
e = Dog('Buddy')

print(f"Dog d kind: {d.kind}")    # shared by all dogs
print(f"Dog e kind: {e.kind}")   # shared by all dogs
print(f"Dog e kind: {Dog.kind}") 

print(f"Dog d name: {d.name}")    # unique to d
print(f"Dog e name: {e.name}")    # unique to e
