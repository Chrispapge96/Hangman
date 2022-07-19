# Write your code here
import random

print("H A N G M A N")
print("The game will be available soon.")
default_commands = {"play", "results", "exit"}
lost = 0
win = 0
while True:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >')

    if command == "play":
        lwords = ("python", "java", "swift", "javascript")
        chosen = random.choice(lwords)
        show = "-" * len(chosen)
        i = 8
        known = set()
        said = set()
        while i > 0:
            print(show)
            letter = input("Input a letter: >")
            if len(letter) > 1 or letter == "":
                print("Please, input a single letter.")
                continue
            if not (letter.isalpha()) or letter.isupper():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if letter in said:
                print("You've already guessed this letter.")
                continue
            if letter in set(chosen):
                indexes = [i for i, c in enumerate(chosen) if c == letter]
                lshow = list(show)
                for j in indexes:
                    lshow[j] = letter
                show = "".join(lshow)
                known.add(letter)
            else:
                print("That letter doesn't appear in the word.")
                i = i - 1

            said.add(letter)  # adds the letter in a set so it knows it's already been guessed

            if known == set(chosen):
                print(show)
                print("You guessed the word {}!\nYou survived!".format(chosen))
                win = win + 1
                break

        if i == 0:
            print("You lost!")
            lost = lost + 1

    elif command == "results":
        print("You won: {} times.\nYou lost: {} times.".format(win, lost))
        continue
    elif command == "exit":
        break
    else:
        continue



