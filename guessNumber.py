# guess magic number games // Beginner coding practice for if- else
import random

magic_number = random.randint(0, 9)
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("guess:"))
    guess_count += 1
    if guess == magic_number:
        print("you Won !!")
        break
else:

    print(f"Try again, magic number is {magic_number}")

