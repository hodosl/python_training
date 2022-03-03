def concatenate_words(words):
    result = ""
    counter = 1
    for word in words:
        result = result + word
        if counter != len(words):
            result += ","
        counter += 1
    return result

print(concatenate_words(["a", "b", "c"]))