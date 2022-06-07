def Main():
    while True:
        try:
            print("\n\nMAIN")
            print('\nEnter "0" to end program.')
            choose = int(input('Enter "1" if Binary to Decimal and "2" if Decimal to Binary: '))
        except Exception:
            print("Choose '0', '1' or '2' only!")  
        else:
            if choose == 0:
                print('==Program Ended==')
                break
            
            elif choose == 1:
                print('\nBINARY TO DECIMAL CONVERSION')
                print('Type "0" to exit.')
                while True:
                    binaryNumber = str(input("\nEnter binary number: "))
                    if binaryNumber == '0':
                        break
                    B2Dconv(binaryNumber)                
                    
            elif choose == 2:
                print('\nDECIMAL TO BINARY CONVERSION')
                print('Type "0" to exit.')
                while True:
                    decimalNumber = str(input("\nEnter decimal number: "))
                    if decimalNumber == '0':
                        break
                    D2Bconv(decimalNumber)
                
                

def B2Dconv(binaryNumber):
    try:
        # binaryNumber input is a string
        # binaryNumber input is indexed and characters are stored as integer in list
        list_binaryNumber = [int(i) for i in binaryNumber]
        # binaryNumber input must all contain integers
        
    except Exception:
        # if there are characters other than an int in input, this function ends
        print("Binary number only!")
        return 1 # why it returns 1? why not? respect my opinion
    
    else:
        # reversed the list of binaryNumber
        list_binaryNumber = listReverse(list_binaryNumber)
        base = 1 # decimal value of 1 in binary place
        decimalValue = 0 # decimalValue is where the decimal values of 1's from the input is stored
        for i in range(len(list_binaryNumber)):
            # STEP 1: list_num indicates the number of index of element
            list_num = list_binaryNumber[i]
            
            #if there are other numbers except 0 and 1 in input, this function ends
            if list_num > 1:
                print("Binary number only!")
                return 1
            
            # STEP 2: if element is 1 in a certain index, equation is used, else, 0 is added
            elif list_num == 1:
                decimalValue += base**list_num
            else:
                decimalValue+=0              
            # decimal value is doubled as binary place increase
            base*=2
            
        # this prints out an integer
        print(decimalValue)
    

def D2Bconv(decimalNumber):
    try:
        decimalNumber = int(decimalNumber)
    except Exception:
        print("Decimal values only!")
        return 1
    else:
        binary_List = [] #List for the binary remainders
        while True:
            quotient = decimalNumber%2
            
            #checks decimal input if it have a remainder or not
            if quotient == 0: 
                decimalNumber//=2 #half the decimal input
                if decimalNumber==0: #decimal input no longer divisible
                    break
                binary_List.append(0) #appends 'zero' remainder
                
            elif quotient == 1:
                decimalNumber//=2 #half the decimal input
                binary_List.append(1) #appends 'one' remainder
        
        convertedBinary = listReverse(binary_List)
        
        #This does not print an integer
        #asterisk prints the list without the square brackets and commas
        print(*convertedBinary, sep='')


#Reverses the binary list just because it is what it is
def listReverse(list_variable):
    list_variable.reverse()
    return list_variable
    

if __name__ == "__main__":
    Main()

