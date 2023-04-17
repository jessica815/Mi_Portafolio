#Area y perimetro de un pentagono sin nada, normalito
if __name__ == "__main__":
    l:float=float(input("Ingresa el valor del lado: "))
    apo:float=float(input("Ingresa el valor del apotema: "))
    P:int=0
    area:int=0
    P=l+l+l+l+l
    print(f"El perimetro es {P}")
    if l<=0:
        print("Error")
        l:float=float(input("Ingresa el valor del lado: "))
        P=l+l+l+l+l
        print(f"El perimetro es {P}")
    if apo<=0:
        print("Error")
        apo:float=float(input("Ingresa el valor del apotema:  "))

    area=P*apo
    P=l+l+l+l+l
    print(f"Area= {area}")
    print(f"El perimetro es= {P}")