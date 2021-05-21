import pandas

nato_DF = pandas.read_csv("nato_phonetic_alphabet.csv")
#    letter      code
# 0       A      Alfa
# 1       B     Bravo
# 2       C   Charlie
# 3       D     Delta
# 4       E      Echo
# 5       F   Foxtrot
# 6       G      Golf
# 7       H     Hotel
# 8       I     India
# 9       J    Juliet
# 10      K      Kilo
# 11      L      Lima
# 12      M      Mike
# 13      N  November
# 14      O     Oscar
# 15      P      Papa
# 16      Q    Quebec
# 17      R     Romeo
# 18      S    Sierra
# 19      T     Tango
# 20      U   Uniform
# 21      V    Victor
# 22      W   Whiskey
# 23      X     X-ray
# 24      Y    Yankee
# 25      Z      Zulu

nato_DF_dict = {row.letter: row.code for index, row in nato_DF.iterrows()}
# {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
# 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M':
# 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S':
# 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
# 'Y': 'Yankee', 'Z': 'Zulu'}

word = input("Enter a word: ")
phonetic_words = [nato_DF_dict[letter] for letter in word.upper()]
print(phonetic_words)



