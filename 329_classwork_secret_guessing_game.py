guess_num = 0
guess_count = 0

while guess_num != 12 and guess_count < 3:
    guess_count += 1
    guess_num = int(input("Nope. Try another number: "))

if guess_count >= 3:
    print("Sorry. You LOSE! Hahaha!")
else:
    print("Congrats!")
