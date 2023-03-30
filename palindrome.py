correct = "NOCABARETERABACON"
wrong = "ABACAXIDOCARALHO"
correctPar = "MACAACAM"

array = []

def palindrome (value):
    
    for i in range(len(value)):
        array.append(value[i])

    n = 0
    k = len(value)-1

    while (n != k):
        if (n >= len(value)/2):
            return print('palindrome')   
        elif(array[n] == array[k]):
            n += 1
            k -= 1      
        else:
            return print('no palindrome')  
    return print('palindrome')  

palindrome(correctPar)