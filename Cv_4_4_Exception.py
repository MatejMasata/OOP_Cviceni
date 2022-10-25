class MyClass():
    pass

a=0

try:
    x=1/a
    a=MyClass()
    b=MyClass()
    c=a+b
    raise NotImplementedError("Abstraktni metoda")
    print("Hotovo")

except ZeroDivisionError:
    print("deleni nulou")

except Exception as e:
    print(f"Nejaky error: {e}")

print("jedeme dal")