#Area y perimetro de un pentagono con do-while
if __name__ == "__main__":
    apo:float=float
    l:float=float
    area:int=0
    P:int=0
    while True:
        l:float=float(input("Ingresa el valor del lado: "))
        if l>0:
            break
    while True:
        apo:float=float(input("Ingresa el valor del apotema: "))
        if apo>0:
            break
    P=l+l+l+l+l
    area=P*apo
    print(f"El area es: {area}")
    print(f"El perimetro es: {P}")