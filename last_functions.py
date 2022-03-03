# szorzótábla
def table():
    for i in range(1,11):
        for j in range(1,11):
            result = i*j
            if result < 10:
                print("", end=" ")
            print(i*j, end=" ")
            j += 1
        i += 1
        print("")


print(table())

