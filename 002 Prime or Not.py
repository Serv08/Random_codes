import numpy as np

print ("Prime number Identifier")
print ("Enter 0 to end program")

while True:
    n = int(input("\nEnter a number: "))
    if n == 0:
        print ("\n==Program Ended==\n")
        break
    else:
        i = 2
        while True:           
            x = n%i
            if n == i:
                print (n, "is Prime.")
                break
            if n == 1:
                print ("1 is neither a prime nor a composite number.")
                break
            if x == 0:
                factorSet = []
                j = 2
                while n >= j:
                    y = n%j
                    if y == 0:
                        factorSet.append(n//j)
                        factorSet.append(j)
                    j+=1
                factorSet.sort()
                print("{} is divisible by {}.".format(n, np.unique(factorSet)))
                break
            else:
                i+=1