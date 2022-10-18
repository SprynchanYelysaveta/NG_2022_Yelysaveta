FirstNumberA = int(input("Enter first number: "))
SecondNumberB = int(input("Enter second number: "))
OperationWithNumbers = input("Choose operation(+, -, *, /, **2, **0.5): ")
if OperationWithNumbers == '+':
    print ("Sum: " + str(FirstNumberA + SecondNumberB))
if OperationWithNumbers == '-':
    print ("Subtraction: " + str(FirstNumberA - SecondNumberB))
if OperationWithNumbers == '*':
    print ("Multiplication: " + str(FirstNumberA * SecondNumberB))
if OperationWithNumbers == '/':
    print ("Division: " + str(FirstNumberA / SecondNumberB))
if OperationWithNumbers == '**2':
    print ("The square of the first number: " + str(FirstNumberA**2))
    print ("The square of the second number: " + str(SecondNumberB**2))
if OperationWithNumbers == '**0.5':
    print ("The square root of first number: " + str(FirstNumberA**0.5))
    print ("The square root of second number: " + str(SecondNumberB**0.5))