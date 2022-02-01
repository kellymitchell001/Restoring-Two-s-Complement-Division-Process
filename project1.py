import copy
from proj1 import restDiv
from proj1 import shifter
from proj1 import subtractor
from proj1 import twoComp

##################    Divide two positive numbers no remainder    ######################

def decimalToBinary(n):
    return bin(n).replace("b","")

print("Divide two positive numbers with no remainder: \n")

Q = int(input("Enter dividend (Q): "))
M = int(input("Enter divisor (M): "))

print("\nValue of Q = ",Q," = 0000", decimalToBinary(Q))
print("Value of M = ",M," = 0000", decimalToBinary(M))

pair=[(M, Q)]
for i in pair:
    results = restDiv(i[0],i[1])
    print("\nInitial Values in registers A, Q, and M:")
    print("A = " + results[0][0] + "  Q = " + results[0][1] + "  M = " + results[0][2])
    
    print("\nFinal cycle of registers Q and A:")
    print("Q = 0000" + results[1][0] + " A = 0000" + results[1][1])

    print("\nFinal Value: " + results[1][0])
    
    print("\nDecimal Format:" + results[2])


##################    Divide two positive numbers w remainder    ######################


print("Divide two positive numbers with remainder: \n")

Q = int(input("Enter dividend (Q): "))
M = int(input("Enter divisor (M): "))

pair=[(M, Q)]

print("\nValue of Q = ",Q," = 0000", decimalToBinary(Q))
print("Value of M = ",M," = 0000", decimalToBinary(M))

for i in pair:
    results = restDiv(i[0],i[1])
    print("\nInitial Values in registers A, Q, and M:")
    print("A = " + results[0][0] + "  Q = " + results[0][1] + "  M = " + results[0][2])
    
    print("\nFinal cycle of registers Q and A:")
    print("Q = 0000" + results[1][0] + " A = 0000" + results[1][1])

    print("\nFinal Value: " + results[1][0])
    
    print("\nDecimal Format:" + results[2])


##################    Divide two negative numbers    ####################################

print("Divide two negative numbers: \n")

Q = int(input("Enter dividend (Q): "))
M = int(input("Enter divisor (M): "))

pair=[(M, Q)]

for i in pair:
    results = restDiv(i[0],i[1])

    print("\nInitial Values in registers A, Q, and M:")
    print("A = " + results[0][0] + "  Q = " + results[0][1] + "  M = " + results[0][2])
    
    print("\nFinal cycle of registers Q and A:")
    print("Q = 0000" + results[1][0] + " A = 0000" + results[1][1])

    print("\nFinal Value: " + results[1][0])
    
    print("\nDecimal Format:" + results[2])

##################    Divide positive number by negative number    ####################################

print("Divide positive number by negative number: \n")

Q = int(input("Enter dividend (Q): "))
M = int(input("Enter divisor (M): "))

pair=[(M, Q)]

for i in pair:
    results = restDiv(i[0],i[1])

    print("\nInitial Values in registers A, Q, and M:")
    print("A = " + results[0][0] + "  Q = " + results[0][1] + "  M = " + results[0][2])
    
    print("\nFinal cycle of registers Q and A:")
    print("Q = 0000" + results[1][0] + " A = 0000" + results[1][1])

    print("\nFinal Value: " + results[1][0])
    
    print("\nDecimal Format:" + results[2])

##################    Divide negative number by positive w/ remainder  ##################

print("Divide negative number by positive w/ remainder: \n")

Q = int(input("Enter dividend (Q): "))
M = int(input("Enter divisor (M): "))

pair=[(M, Q)]

for i in pair:
    results = restDiv(i[0],i[1])

    print("\nInitial Values in registers A, Q, and M:")
    print("A = " + results[0][0] + "  Q = " + results[0][1] + "  M = " + results[0][2])
    
    print("\nFinal cycle of registers Q and A:")
    print("Q = 0000" + results[1][0] + " A = 0000" + results[1][1])

    print("\nFinal Value: " + results[1][0])
    
    print("\nDecimal Format:" + results[2])

