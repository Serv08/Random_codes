while True:
    lastDigits = int(input("\nEnter desired last digits of the number: "))
    
    if lastDigits%2 == 0:
        print ("The last digit cannot be even.")
    elif lastDigits%5 == 0:
        print ("5 cannot be the last digit.")    
        
    elif lastDigits%5 or lastDigits%2 != 0:
        numOfPrimes = int(input("\nInput desired number of primes: "))
        primesSet = []
        n = 0
        
        while len(primesSet) < numOfPrimes:
            combinedDigitsStr = (str(n)+str(lastDigits))
            combinedDigitsInt = int(combinedDigitsStr)              
            n+=1
            j = 2
            
            while True:                
                x = combinedDigitsInt%j
                if combinedDigitsInt == j:
                    primesSet.append(combinedDigitsInt)
                    break
                if x == 0:
                    break
                else:
                    j+=1
                            
        print(primesSet)                     
        break