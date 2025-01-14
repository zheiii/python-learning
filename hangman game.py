words = ["banana", "python", "hangman", "apple"]
import random
random_index = random.randint(0, len(words)-1)
secret_word = words[random_index]
lives = 6
output_index = 0
right_guesses = 0
guessed_letters = set()
charachters = len(secret_word)
output = "- "*charachters
output = output.split()
print("".join(output))
letters = set(secret_word)

while lives > 0 :
    letter = input("guess:")
    if letter in guessed_letters:
        print("you've already guessed that word")
    elif letter in secret_word and letter != " " :
        right_guesses = right_guesses+1
        for output_index in range(charachters):
            if secret_word[output_index] == letter:
                output[output_index] = letter
                guessed_letters.add(letter)
        print("".join(output))
        if right_guesses == len(letters):
            print("there you go!")
            break            
    else:
        print("wrong:(")
        guessed_letters.add(letter)
        lives = lives-1
else:
    print("oops! you ran out of guesses.")

