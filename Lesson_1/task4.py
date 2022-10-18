NumberA = input("Enter number A: ")
NumberB = input("Enter number B: ")
NumberC = input("Enter number C: ")
NumberA = float(NumberA)
NumberB = float(NumberB)
NumberC = float(NumberC)
Discriminant = NumberB**2 - 4*NumberA*NumberC
print ("Discriminant: " + str(Discriminant))
if Discriminant < 0:
    print ("There are no roots")
elif Discriminant == 0:
    x = -NumberB/(2*NumberA)
    print ("x= :" + str(x))
else:
    x1 = (-NumberB+Discriminant**0.5)/(2*NumberA)
    x2 = (-NumberB-Discriminant**0.5)/(2*NumberA)
    print ("x1= :" + str(x1))
    print ("x2= :" + str(x2))
    