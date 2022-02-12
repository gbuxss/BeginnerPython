# guess magic number games // Beginner coding practice for if- else
magic_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("guess:"))
    guess_count += 1
    if guess == magic_number:
        print("you Won !!")
        break
else:
    print("Try again")

