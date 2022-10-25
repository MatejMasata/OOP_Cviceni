"""ZÁKLADY"""

print("hello world")

a=1
b="pes"
c="jak udelat uvozovky\""       #zpetne lomitko - AltGr+Q

print(a)
print(b)
print(a,b)

"""DATOVÉ TYPY"""

i=1                 #int
f=2.3               #float
c=2.5+1.3j          #complex
b=True              #bool
s="kocicka"         #string

print(type(i))
print(type(f))
print(type(c))
print(type(b))
print(type(s))

print(False==0)     #True
print(1=="1")       #False

"""print F"""
x=1
y=2
z=3

print(f"Moje cisla jsou {x}, {y} a {z}")

"""OPERATORY"""

x=5
y=3

print(x+y)
print(x-y)
print(x*y)
print(x/y)

print(x**y)     #x^y
print(x%y)      #modulo zbytek
print(x//y)     #floor

x+=y
print(x)

x**=y
print(x)

