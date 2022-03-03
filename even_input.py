number = 0
while number == 0:
    number = int(input("Adj meg egy számot: "))
    if number == "":
        print("Nem adtál meg számot")
if number % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")

year = int(input("Add meg a szuletesi eved:"))
min_year = 1900
act_year = 2022
if (year > act_year or year < min_year):
    print("Helytelen szuletesi ev!")
else:
    print("Az eletkorod", 2022 - year, "év")