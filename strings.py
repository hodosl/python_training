# name = "John Doe"
#
# print(name.upper())
# print(name.lower())
#
# print(name[0])
#
# for c in name:
#     print(c)
# # szeletelés = slicing
# print(name[0:4])
# print(name[:6])
# print(name[0:7:2]) # 0-7 ig minden másodikat
# print(name[::-1]) # visszafelé írja ki
#
# word = "haliho"
# print(word[:-1]) # végéből lecsíp egyet (visszafelé -1)
#
# ip = "192.168.0.1"
# print(ip[-1:])
#
# print("a" in "alma") # a szerepel az alma stringben

## Írj egy olyan függvényt, ami megszámolja, hogy
## hány darab a betű van egy szóban!

def count_a(word):
    counter = 0
    for c in word:
        if c == "a":
            counter += 1
    print(counter)

count_a("amarath")

## Írj egy olyan függvényt, amely paraméterül kap
## egy szót, és megszámolja, hogy hány magánhangzó van benne


def count_vowel(word):
    counter = 0
    for c in word:
        if c in "aeiou":
            counter += 1
    print(counter)


count_vowel("kutyafule")

## Írj egy függvényt, mely kap egy szót, és visszaadja
## a benne szereplő betűket *-gal elválasztva egy stringben!
## Az utolsó karakter után ne legyen *
## xyz -> x*y*z

#result = ""
#végigmenni a szón ha nem " " hozzákon

def caracter_1(word):
    string = ""
    for c in word:
        if c != " ":
            string += c + "*"
    print(string[:-1])

caracter_1("x z y")

## Írj egy függvényt, amely visszaadja, hogy a paraméterként
## átadott szó megfordítva is ugyanaz-e

# def is_reverse_equal(word):
#     retutn word == word [-1]

## Írj egy függvényt, ami a paraméterként átadott szóból
## kiveszi a space-eket, és azt adja vissza.
def kill_spaces(word):
    string = ""
    for c in word:
        if c != " ":
            string += c
    return string

name = "John Doe"
print(name.index("Doe")) # 5. karakter a D

print("alma korte barack".split())
fruit = "alma korte barack"
fruit_list = fruit

for n in fruit_list:
    print(n)

ip ="192.168.0.1"
print(ip.split(".")) # elválaztó karakter a pont
for number in ip.split("."):
    print(int(number))

