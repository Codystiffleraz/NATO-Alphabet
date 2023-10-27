import pandas
# Converts csv to DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Converts DataFrame to dict in {A: "Alpha"} format
words = {row.letter:row.code for (index, row) in data.iterrows()}    
# User input for a word
user_input = input("Type a word :").upper()
# Pulls the value from the key and adds it to a list from the typed user input
new_list = [words[letter] for letter in user_input]
print(new_list)
