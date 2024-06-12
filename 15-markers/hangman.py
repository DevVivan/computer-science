import random
HANGMAN = ['''  +---+  |   |      |      |      |      |=========''', '''  +---+  |   |  O   |      |      |      |=========''', '''  +---+  |   |  O   |  |   |      |      |=========''', '''  +---+  |   |  O   | /|   |      |      |=========''', '''  +---+  |   |  O   | /|\  |      |      |=========''', '''  +---+  |   |  O   | /|\  | /    |      |=========''', '''  +---+  |   |  O   | /|\  | / \  |      |=========''']
words = ["beautiful", "majestic", "unfortunately"]
randomWordIndex = random.randint(1, len(words))
randomWord = words[randomWordIndex]
length = len(randomWord)
counter = 0
guessedWord = ""

while counter < length:
    guessedWord = guessedWord + "_"
    counter = counter + 1

print(guessedWord)