import random
import numpy 
M = random.randrange(4,5)
N = M
count=0
b=0
print("M = ",M)
a = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(-5,8)
print(a)
while count+1!=M:

    print(a[0][j-count])
    count+=1
    if a[0][j-count]<0:
        b+=1
        print(b)


      

   
    
