print("Gondolj egy számra 1 és 10 között")
max_guess = 10
min_guess = 1
guess = 5
answer = "x"
while answer != "E":
    guess = int((min_guess + max_guess) // 2)
    print("A tippem ", guess)
    answer = input("[K]isebb, [N]agyobb vagy [E]gyenlő: ")
    if answer == "K":
        max_guess = guess - 1
    elif answer == "N":
        min_guess = guess + 1
print("A gondolt szám ", guess)
