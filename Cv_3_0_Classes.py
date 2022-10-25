class MyClass:
    my_atribute=5

    def my_method(self):
        print("method of a class")


my_object=MyClass()
my_object.my_method()
print(my_object.my_atribute)        # Atribut objektu
print(MyClass.my_atribute)          # Atribut třídy

my_object.my_atribute=10            # Přepsání atributu pouze u mého  objektu
print(my_object.my_atribute)        
print(MyClass.my_atribute)

MyClass.my_atribute=77              # Přepsání atributu u třídy
print(my_object.my_atribute)        
print(MyClass.my_atribute)
