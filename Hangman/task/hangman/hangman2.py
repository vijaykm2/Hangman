import random

# print()
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
random.seed()
selection = ''
length = 0
replacement = "-" * length
# print("\n" + replacement)

inputs = set()
count = 8
play = True

play_str = input('Type "play" to play the game, "exit" to quit:')
if play_str == "play":
    play = True
elif play_str == "exit":
    play = False


def get_replacement():
    global replacement
    for char in inputs:
        if selection.find(char) != -1:
            for i in range(0, length):
                ch = selection[i]
                if ch == char:
                    if len(replacement) != len(selection):
                        replacement += ch
                    else:
                        replacement = replacement[:i] + ch + replacement[i + 1:]
                else:
                    if len(replacement) != len(selection):
                        replacement += "-"


def play_game():
    global count, replacement, inputs, selection
    while count > 0:
        letter = input("Input a letter : ")
        otherError = False
        if len(letter) != 1:
            print("You should input a single letter")
            otherError = True

        if not letter.islower():
            print("It is not an ASCII lowercase letter")
            otherError = True

        if replacement.find("-") == -1:
            if count > 0:
                count -= 1
                print("\n")
                print(replacement)
                continue
            else:
                break
        # else:
        #     replacement = ""

        if letter not in selection and not otherError:
            alreadyTyped = False
            if letter in inputs:
                print("You already typed this letter")
                alreadyTyped = True

            print("No such letter in the word")

            if replacement == "":
                replacement = "-" * length
            else:
                get_replacement()
            if count > 1 or alreadyTyped:
                print("\n")
                print(replacement)

            if not alreadyTyped:
                count -= 1
                inputs.add(letter)
            continue
        elif letter in inputs:

            print("You already typed this letter")
            print("\n")
            print(replacement)
            # count -= 1
            continue

        inputs.add(letter)
        get_replacement()

        print("\n")
        print(replacement)

        if replacement == selection:
            break

    # print()
    if replacement == selection:
        print('''You guessed the word!
You survived!''')
    else:
        print("You are hanged!")
    play_str = input('Type "play" to play the game, "exit" to quit:')
    global play
    if play_str == "play":
        play = True
    elif play_str == "exit":
        play = False


while play:
    selection = random.choice(words)
    length = len(selection)
    replacement = "-" * length
    print("\n" + replacement)

    inputs = set()
    count = 8
    play_game()
