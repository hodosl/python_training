names = []

names.append("John Doe") # hozzáadás a listához
print(names)

names.append("Jack Doe") # hozzáadás a listához
print(names)

print(names[0]) # lista 0. eleme

names[1] = "jack smith"
print(names)

names.remove("jack smith")
print(names)

len(names) #lista hossza

print("John Doe" in names) # true mert benne van

# filter
#["John Smith", "Jane Smith", "Jack Doe", "John Doe"]
#["John Smith", "John Doe"]

def john(names: names) -> list:
    result = []
    for c in names:
        if "John" in c and c.index("John") == 0:
            result.append(c)
    return result

print(john(["John Smith", "Jane Smith", "Jack Doe", "John Doe"]))

