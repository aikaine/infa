import random

N = int(input('Введите количество строк: '))
M = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 10) for _ in range(M)] for _ in range(N)]
def sum_el(lst):
    total = 0
    for elem in lst:
        if elem > 0 and elem % 2 == 0:
            total += elem
    return total

def sort(lst):
    n = len(lst)
    character = [sum_el(row) for row in lst]




    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if character[j] > character[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                character[j], character[j + 1] = character[j + 1], character[j]
    return lst


print("Исходный список:")
for row in matrix:
    print(row)

sorted_list = sort(matrix)

print("\nИзмененный список:")
for row in sorted_list:
    print(row)
