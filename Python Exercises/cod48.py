#Area y perimetro de un rombo con do-while
if __name__ == "__main__":
    D:float=float
    dm:float=float
    l:float=float
    area:int=0
    P:int=0
    while True:
        D:float=float(input("Ingresa el valor de la diagonal mayor: "))
        if D>0:
            break
    while True:
        dm:float=float(input("Ingresa el valor de la diagonal menor: "))
        if dm>0:
            break
    while True:
        l:float=float(input("Ingresa el valor del lado: "))
        if l>0:
            break
    area=D*dm
    P=l+l+l+l
    print(f"El area es: {area}")
    print(f"El perimetro es: {P}")