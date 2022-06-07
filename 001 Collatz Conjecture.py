#Collatz Conjecture
#Iteration Counter
#Largest number identifier (positive)
#Lowest number identifier (negative)

i = 0
n = float(input("Enter Number: "))

n_Set = []

if n>0:
    while n>1:
        if n%2==0:
            n = n/2
            i+=1
            n_Set.append(n)
            print(n)
        elif n%2==1:
            n = (3*n)+1
            i+=1
            n_Set.append(n)
            print(n)
        largestNum = int(max(n_Set))
elif n<0:
    while n<-1:
        if n%2==0:
            n = n/2
            i+=1
            n_Set.append(n)
            print(n)
        elif n%2==1:
            n = (3*n)+1
            i+=1
            n_Set.append(n)
            print(n)
        smallestNum = int(min(n_Set))

print ("Number of Iterations:\t", i)
if n>0:
    print ("Largest Number:\t\t", largestNum)
elif n<0:
    print ("Smallest Number:\t", smallestNum)