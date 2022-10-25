class Dog:

    kind = 'canine'
    
    def __init__(self, name):  # instance method
        self.name = name 
    
    def get_name(self):  # instance method
        return self.name
    
    @classmethod
    def get_kind(cls):  # class method
        return cls.kind
    
print(f"Any dog's kind is: {Dog.get_kind()}")  # calling class method over class

dog_buddy = Dog("Buddy")
print(f"Dog named {dog_buddy.get_name()} is of kind: {dog_buddy.get_kind()}")  # calling class method over instance -> instance has access to everything, its class has access to

"""
print(f"Any dog's name is: {Dog.get_name()}") # calling instance method over class -> THIS WILL FAIL, CLASS CANNOT ACCESS INSTANCE PROPERTY
"""