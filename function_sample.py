# Hozz létre egy is_even nevű függvényt,
# amely True-t ad vissza, ha a paraméterként megadott
# érték páros, egyéb esetben False-t adjon vissza
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
def is_even(number):
    return number % 2 == 0

# Hozz létre egy sum_negatives függvényt, mely paraméterül kap egy listát,
# és összegzi a benne szereplő negatív számokat, és azzal tér vissza

def sum_negatives(list):
    sum = 0
    for i in list:
        if i < 0:
            sum = sum + i
    return sum


# Hozz létre egy to_minutes függvényt, mely paraméterül megkapja
# az órák számát, és visszatér a percek számával

def to_minutes(hours):
    minutes = hours * 60
    return minutes

# Hozz létre egy input_number függvényt, melynek legyen egy
# paramétere. A függvény bekér a felhasználótól egy szöveget
# a paraméterrel megadott szöveggel, számmá konvertálja és azt adja vissza


def input_number(message):
    return int(input(message))

print(type(input_number(("adj meg egy számot: "))))

# Írjatok egy annotate_every_even_number függvényt, mely kap egy
# számok listáját, és kiírja őket egymás alá, de minden másodikat
# egy karakterrel beljebb ír ki

def annotate_every_even_number(list):
    counter = 1
    for i in list:
        if is_even(counter)
            print(" ", i)
        else:
            print(i)
        counter += 1



#print(is_even(7))
list = [1,-2, 5, -4, 8, 10]
print(sum_negatives(list))

#print(to_minutes(7))
print(annotate_every_even_number(list))

# Írj egy concatenate_shorts függvényt, mely paraméterül kap szavak listáját
# és csak a 3 karakternél rövidebb szavakat fűzze össze egy stringbe,
# és ezt adja vissza

def concatenate_shorts(words):
    result = ""
    for word in words:
        if len(word) <= 2:
            result = result + word + ","
    return result
