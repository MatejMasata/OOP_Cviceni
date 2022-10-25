"""
Create unique usernames:
1) Write a function which creates new key-values called usernames, which should be unique. Input data are stored in a dictionary
2) login is composed of first 5 letters of surename and first 3 letters of first name
"""
# DEFINICE FUNKCE
def unique_username(dict):

    # DETEKCE AKTIVNICH UCTU
    # Predpoklad:   1) delka hodnot "students" a "active" je stejna
    a_students=[]
    a_active=[]
    for x in range(len(dict["active"])):

        if data["active"][x]:
            a_students.append(dict["students"][x])
            a_active.append(dict["active"][x])

    new_data={}                         # Slovnik pro upravena data
    new_data["students"]=a_students
    new_data["active"]=a_active

    # VYTVORENI PREZDIVEK
    # Predpoklady:  1) Pouze jmeno a prijmeni, NE druhé jméno, titul...
    #               2) Krestni jmeno min 3 znaky, prijmeni min 5 znaku
    #               3) Pokud ma vice jak 10 lidi stejne jmeno, tak se nahrazuje stale jen posledni znak dvojici, trojici... cisel
    new_data["usernames"]=[]

    for x in range(len(new_data["students"])):

        name=new_data["students"][x]
        name=name.lower().split()                               # Vse na mala pismena a rozdeleni jmena do listu - [jmeno,prijmeni]

        first3=name[0][:3]
        first2=name[0][:2]
        surname5=name[1][:5]

        username=surname5+first3

        if username not in new_data["usernames"]:               # Pokud jmeno neexistuje - prirazeni k uzivateli
            new_data["usernames"].append(username)
        else:                                                   # Pokud jiz existuje - posledni znak se nahradi postupne rostoucim cislem
            count=1
            username_num=surname5+first2+str(count)
            while username_num in new_data["usernames"]:
                count+=1
                username_num=surname5+first2+str(count)
            new_data["usernames"].append(username_num)

    return new_data

# TEST FUNKCE
data = {
    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere","John Deere", "Pavel Novak", "pavel novak", "pavel Novak", "PAVEL NOVAK"],
    "active":[True, False, True, True, False, True, True, True, False]
}
test=unique_username(data)
print(test)