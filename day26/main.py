import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

print(nato_alphabet)

word = input("Enter a word to convert to NATO alphabet: ")

nato_word = [nato_alphabet[letter.upper()] for letter in word]

print(nato_word)
