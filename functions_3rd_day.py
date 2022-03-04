# # Írjatok egy get_max nevű függvényt,
# # aminek paraméterül át lehet adni két
# # lebegőpontos számot, és adja vissza a
# # kettő közül a nagyobbat!

def get_max(a: float, b: float) -> float:
    if a > b:
        return a
    else:
        return b

print(get_max(3.2,4.6))
print(get_max(7.28,3.14))

# Írjatok egy beszédes print_square függvényt,
# ami paraméterül kap két egész számot.
# Rajzoljon ki egy ekkora téglalapot, csillagokból.
# 7, 5
#
# *******
# *     *
# *     *
# *     *
# *******

def print_square(a,b):
    counter = 1
    string_a = a * "*"
    string_b = "*" + (a-2)* " " + "*"
    while counter != b+1:
        if counter == 1:
            print(string_a)
        elif counter == b:
            print(string_a)
        else:
            print(string_b)
        counter += 1

def print_square2(width: int, height: int) -> None:
    def p():
        print("*")
    def p2():
        print("*", end="")
    # felső oldal
    for i in range (0, width):
        p2()
    print()
    # közbölső sorok
    for j in range(0, height - 2):
        p2()
        for i in range (0, width - 2):
            print(" ", end="")
        p()
     # alsó sorok
    for i in range(0, width):
        p2()
    print()

print_square2(3, 4)

# Írjatok egy függvényt ami paraméterül megkapja a szavak listáját és visszaadja ezeket összefűzve, de mindegyiket gondolatjel között
# -alma--korte--meggy-

def repeat_words_with_hyphens(words: list) -> str:
    result = " "
    for word in words:
        result += "-" + word +"-"
    return result

