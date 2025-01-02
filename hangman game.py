secret_word = "python"
lives = 6
output_index = 0
right_guesses = 0
guessed_letters = set()
letters = set(secret_word)
win_point = len(letters)
charachters = len(secret_word)
output = "- "*charachters
output = output.split()

while lives > 0 :
    letter = input("guess:")
    if letter in secret_word:
        right_guesses = right_guesses+1
        for output_index in range(len(secret_word)):
            if secret_word[output_index] == letter:
                output[output_index] = letter
                print("".join(output))
                guessed_letters.add(letter)
                lives = lives-1
        
    elif letter in guessed_letters:
        print("you've already guessed that word")
    else:
        print("wrong:(")
        guessed_letters.add(letter)
        lives = lives-1
else:
    if right_guesses == win_point:
                    print("there you go!")
    else:
        print("oops! you ran out of guesses.")

