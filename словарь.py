string = input("Введите строку: ")
dictionary = {}

for index, letter in enumerate(string):
    if letter not in dictionary:
        dictionary[letter] = []
    dictionary[letter].append(index)
    

print(dictionary)
