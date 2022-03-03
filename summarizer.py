number = 0
while number == 0:
    number = int(input("Add meg hány számmal szeretnél dolgozni: "))
    if number == "":
        print("Nem adtál meg számot")
sum = 0
for i in range(number):
    input_number = int(input("Add meg a " + str(i+1) + " számot: "))
    if input_number > 0:
        sum = sum + input_number

#sum = number_1 + number_2 + number_3
print("Összesen:", sum) # számok összege a listából