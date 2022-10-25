""" While, for """

coins = 3

while coins > 0:
    print(f'Go by bus. Only {coins} coins left')
    coins -= 1
print('No coins remaining')





storage = ['Box','Car','Dog','Cat']
for i in range(0, len(storage)):
    print(f'There is a {storage[i]} in the storage')




for item in enumerate(storage):
    print(item)

print()
for item in enumerate(storage,start=5):
    print(item)

storage = ['Box','Car','Dog','Cat']
for index, item in enumerate(storage):
    print(f'There is a {item} in the storage -> {index+1}/{len(storage)}') # the reason why we add +1 to index is that basic indexing goes from 0
