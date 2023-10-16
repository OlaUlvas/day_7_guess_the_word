import random
from guess import logo
from guess_words import word_list

print("\nWelcome to ")
print(logo)
print("\nYou have to find the right word in 10 attempts to win.\n")

attempt = 10
rand_word = random.choice(word_list).lower()
display = []

for letter in rand_word:
    display += "_"

game_on = True
while game_on:

    print(display)

    print(f"Ppst...the word is {rand_word}")
    guess = input("Guess a letter ").lower()

    for position in range(len(rand_word)):
        letter = rand_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in display:
        attempt -= 1

    if "_" not in display:
        print(display)
        print("You Win.")
        sub = 10 - attempt
        print(f"with only {sub} misses.")
        game_on = False

    if attempt < 1:
        print("You Lose.")
        game_on = False








