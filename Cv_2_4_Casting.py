# Casting - change data types

x=1
print(type(x))
print(type(float(x)))
print(type(str(x)))

x=1
print(str(x)+" Hello")

# Pozor na tento převod 
x=1.234
print(int(x))

# NEFUNGUJE TO JAKO ZAOKROUHLOVANI!!
x=1.98
print(int(x))