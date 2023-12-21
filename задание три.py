import random
def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)
a = random.randint(10,15)
b = random.randint(10,15)
c = random.randint(10,15)
d = random.randint(10,15)
result_ab = nod(a, b)
result_ac = nod(a, c)
result_ad = nod(a, d)
print('a= ',a,'b=',b,'c=',c,'d=',d)

print("НОД(a, b) =", result_ab)
print("НОД(a, c) =", result_ac)
print("НОД(a, d) =", result_ad)
