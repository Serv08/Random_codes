print ("Number of Primes")
print ("Enter 0 to end program")

while True:
    numPrimes = int(input("\nEnter how many primes: "))
    primeSet = []
    m = 1
    
    if numPrimes == 0:
        print ("\n==Program Ended==\n")
        break
    else:
        for j in range(numPrimes):
            while len(primeSet) < numPrimes:
                m += 1                
                i = 2
                while True:           
                    x = m%i
                    if m <= i:
                        primeSet.append(m)
                        break
                    if x == 0:
                        break
                    else:
                        i+=1            
        print(primeSet)