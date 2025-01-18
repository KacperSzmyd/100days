import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_nato_spelling():
    word = input("Enter a word to convert to NATO alphabet: ")
    try:
        nato_word = [nato_alphabet[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only alphabet letters please.")
        generate_nato_spelling()
    else:
        print(nato_word)


generate_nato_spelling()
