# Zakladni funkce
def moje_funkce(number):
    print(f"Vstup je: {number}")
    return number**2

vysledek=moje_funkce(67)
print(vysledek)

# Proměnný počet vstupů - HVEZDICKA BY MELA BYT NA KONCI !!
def suma_cisel(zakladni_hodnota,*nums):
    num_sum=zakladni_hodnota
    for num in nums:
        num_sum+=num
    return num_sum

print(f"Soucet je: {suma_cisel(100,6,9,1)}")

# Proměnný počet vstupů - KDYZ NENI HVEZDICKA NA KONCI!!
def suma_cisel(*nums,zakladni_hodnota):
    num_sum=zakladni_hodnota
    for num in nums:
        num_sum+=num
    return num_sum

print(f"Soucet je: {suma_cisel(100,6,9,zakladni_hodnota=1)}")

# Defaultni hodnota - když na nejakou pozici nic nezadam
def default_hod(base_value=2):
    print(base_value)

default_hod()
default_hod(6)