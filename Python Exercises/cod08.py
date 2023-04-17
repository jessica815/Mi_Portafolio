#Obtener la tabla de multiplicar de n hasta el 5

if __name__ == "__main__":
    n:int=int(input("Ingrea n: "))
    while n<0:
        print("Error")
        n:int=int(input("Ingresa n: "))

    while n>0:
        break
    for c in range (1,6):
        print (f"{n} x {c} = {n*c}")
    

