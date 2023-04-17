#Calculadora sencilla que reciba 2 números enteros positivos. 

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

n1:int = int(input("Dame un numero: "))
n2:int = int(input("Dame otro numero: "))

print(f"{n1}+{n2}={suma(n1,n2)}")
print(f"{n1}-{n2}={res(n1,n2)}")
print(f"{n1}*{n2}={mul(n1,n2)}")
print(f"{n1}/{n2}={div(n1,n2)}")
print(f"{n1}^{n2}={pot(n1,n2)}")