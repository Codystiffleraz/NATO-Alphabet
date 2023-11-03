import pandas
# Converts csv to DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Converts DataFrame to dict in {A: "Alpha"} format
words = {row.letter:row.code for (index, row) in data.iterrows()}    


def generate_phonetic():
    # User input for a word
    user_input = input("Type a word: ").upper()
    try:
        # Pulls the value from the key and adds it to a list from the typed user input
        new_list = [words[letter] for letter in user_input]
    except KeyError:
        # Validates the input is a letter if not prints type a letter and repeats the input
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)

generate_phonetic()
