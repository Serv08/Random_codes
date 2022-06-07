import numpy as np

print ("Factors Determiner")
print ("Enter 0 to end program")

while True:
    n = int(input("\nInput a number to be factored: "))
    if n == 0:
        print ("\n==Program Ended==\n")
        break
    else:
        factorSet = []
        j = 2
        while n >= j:
            y = n%j
            if y == 0:
                factorSet.append(n//j)
                factorSet.append(j)
            j+=1
        
    factorSet.sort()
    print(np.unique(factorSet))
