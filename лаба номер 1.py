import math
import random
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
numbers = []
for _ in range(10):  
    number = random.randint(1, 15)  
    numbers.append(number)
print(numbers)
count = 0
for num in numbers:
    if isprime(num):
        count += 1
print("Количество простых чисел",count)
