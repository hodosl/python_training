def print_employee_data(name, age):  # függvény definiciója, paraméter nevek
    print("az alkamazott neve: ", name)
    print("az alkamazott eletkora: ", age)
    # függvény végén a paraméterek törlődnek


def print_dog_name(name):
    print("a kutya neve: ", name)


def print_a_es_B(a,b):
    print("a két szám összege: ", (a+b))


def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

print_a_es_B(12,1)

#print_employee_data("John", 10)  # paraméter értékek

