
def test(a,b):
    return a+b

print(test(3,6))

#Lambda - funkce se pouzije jen jednou 
print((lambda a,b:a+b)(1,3))

data=[(2,"kocka"),(8,"pes"),(1,"ptacek")]
print(f"puvodni poradi: {data}")
print(f"srovnany podle cisla: {sorted(data)}")
print(f"srovnany podle cisla: {sorted(data, key=lambda x:x[1])}")

