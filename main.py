
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for (index, row) in df.iterrows()}
word = input("Enter a word: ").upper()
letter = word.split()
list = [phonetic_alphabet[letter] for letter in word ]
print(list)
