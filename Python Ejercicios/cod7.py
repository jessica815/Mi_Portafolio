#Calculadora sencilla que reciba 2 números enteros positivos. Asumiendo que se capturan datos válidos.

n1:int = int(input("Dame un numero: "))
while n1<0:
    print("Error")
    n1:int = int(input("Dame un numero: "))

n2:int=int(input("Dame otro número: "))
while n2<0:
    print("Error")
    n2:int=int(input("Dame otro número: "))

def suma(num1:int, num2:int)->int:
    return num1+num2

def res(num1:int, num2:int)->int:
    return num1-num2

def mul(num1:int, num2:int)->int:
    return num1*num2

def div(num1:int, num2:int)->int:
    return num1/num2

def pot(num1:int, num2:int)->int:
    return num1**num2

print(f"{n1}+{n2}={suma(n1,n2)}")
print(f"{n1}-{n2}={res(n1,n2)}")
print(f"{n1}/{n2}={div(n1,n2)}")
print(f"{n1}^{n2}={pot(n1,n2)}")