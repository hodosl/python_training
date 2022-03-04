# Írj egy olyan is_ascending függvényt, mely paraméterül kap
# három egész számot. A függvény True-t ad vissza,
# ha a számok szigorúan növekvő sorrendben vannak.
# Ellenkező esetben visszaad egy False értéket.
# 1, 3, 6 -> True
# 1, 10, 20 -> True
# 1, 1, 1 -> False
# 20, 10, 1 -> False
# 20, 10, 20 -> False
def is_ascending(word1, word2, word3):
    result = word3 > word2 > word1 #return a < b < c
    return result

is_ascending(20,10,1)
# Írj egy word_concat függvényt, mely két szót kap
# paraméterként, és visszaadja őket összefűzve úgy,
# hogy a rövidebb legyen elől
# "alma", "korte" -> "almakorte"
# "cseresznye", "meggy" -> "meggycseresznye"
# "korte", "meggy" -> kortemegy

def word_concat(word1, word2):
    if len(word1) > len(word2):
        return word2 + word1
    else:
        return word1 + word2

