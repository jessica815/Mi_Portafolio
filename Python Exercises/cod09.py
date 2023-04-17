#Obtener la tabla de multiplicar n hasta el 5

if __name__ == "__main__":
    while True:
        n:int=int(input("Dame un numero: "))
        if n>0:
            break
    for c in range(1,6,1):
        print (f"{n} x {c} = {n*c}")