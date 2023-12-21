text = input("Введите предложение или строку: ")
words = text.split()
result = []
for word in words:
    count = 0 
    for letter in word:   
        if letter == 'а':
            count += 1
    if count >= 2:
        result.append(word)
print("Слова, в которых буква 'а' встречается не менее двух раз:", result)
