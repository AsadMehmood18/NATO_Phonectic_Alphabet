
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for (index, row) in df.iterrows()}
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list = [phonetic_alphabet[letter] for letter in word ]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list)
generate_phonetic()
