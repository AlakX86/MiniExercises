def print_multiplication_table(multiplicationNum):
    multiplicationNum = 1
    multiplicationCounter = 0
    while multiplicationNum <= multiplicationNum:
        if multiplicationNum != multiplicationCounter:
            multiplicationCounter = multiplicationCounter + 1
            total = multiplicationNum * multiplicationCounter
            print(str(multiplicationNum) + "*" + str(multiplicationCounter) + "=" + str(total))
        else:
            multiplicationNum = multiplicationNum + 1
            multiplicationCounter = 0  
print_multiplication_table(4)

#Necesitamos una tabla sistematica, que multiplique desde el 1
#hasta el infinito y luego unos multiplicandos que multipliquen
#hasta un numero indicado