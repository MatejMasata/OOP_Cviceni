list_example=[1,2,3,"hello"]
print(list_example)

#na druhou pozici přiřadíme (nahradíme) 854
list_example[1]=854
print(list_example)

#přidáme další pozici (imaginární číslo)
list_example.append(0.1+0.2j)
print(list_example)

#přidáme na určitou pozici
list_example.insert(2, "tohle vkládám")
print(list_example)

#odebereme 3 pozici
list_example.pop(2)         #nebo: del list_example[2]
print(list_example)

#odebereme poslední poslední pozici
list_example.pop()
print(list_example)



