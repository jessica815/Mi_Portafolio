#Tabla de multiplicar n hasta n números

if __name__ == "__main__":
    n:int = int(input("Dame un numero: "))
    lf:int = int(input("Hasta que numero quieres llegar?: "))
    for i in range(1,lf+1):
        print(f"{n} x {i} = {n*i}")
    