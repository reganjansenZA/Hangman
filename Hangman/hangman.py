import random

words = ['stormers' , 'bulls' , 'sharks' , 'lions' , 'cheetahs']

# randomly choose a word from the list

chose_word = random.choice(words)
word_display = ['_' for _ in chose_word]
attempts = 5

print('Welcome to Hangman - SA Rugby Team Edition')

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter").lower()
    if guess in chose_word:
        for index, letter in enumerate(chose_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Weet jou pa dat jy hoe DOM is!")
        attempts -= 1

# End of game

if '_' not in word_display:
    print("DRIEEE PUNTE")
    print(' '.join(word_display))
    print("SKINK A DOP!!!!")

else:
    print('Jou kanse is op meneer')
    print("Gaan huil by die huis")
