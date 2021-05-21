import pandas
nato_DF = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_DF_dict = {row.letter: row.code for index, row in nato_DF.iterrows()}

word = input("Enter a word: ")
phonetic_words = [nato_DF_dict[letter] for letter in word.upper()]
print(phonetic_words)
