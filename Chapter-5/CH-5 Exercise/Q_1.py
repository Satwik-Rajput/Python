dictionary = {
    "Kalam": "Pen",
    "Kitaab": "Book",
    "Mez": "Table",
    "Kursi": "Chair",
    "Pankha": "Fan"
}

word = input("Enter a Hindi word: ")
print("English meaning:", dictionary.get(word, "Word not found in dictionary."))
