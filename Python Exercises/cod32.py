#Obtenga x^y por medio de sumas sucesivas. Indicando cuantas
# veces se sumó con do-while

if __name__ == "__main__":
    while True:
        x=input("Ingresa un número x: ")
        try:
            x=int(x)
            break
        except ValueError:
            print("Ingresa un número entero: ")
    while True:
        y=input("Ingresa la potencia y: ")
        try:
            y=int(y)
            break
        except ValueError:
            print("Ingresa un número entero: ")
    num=x
    aux=x
    if y==0:
        print(1)
    else:
        for i in range(1,y):
            print(i)
            for c in range(1,x):
                print(f"{num} + {aux}")
                num=num+aux
            aux=num
        print(num)
