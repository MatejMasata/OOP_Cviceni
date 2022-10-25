"""
FizzBuzz
cisla od 1 do FinalNumber
pokud deletelne 3       ---> Fizz
pokud delitelne 5       ---> Buzz
pokud delitelne 3 i 5   ---> Fizz Buzz

"""

FinalNumber=100

for num in range(1,FinalNumber):

    if num%3==0 and num%5==0:
        print("Fizz Buzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

print("Printing finished")