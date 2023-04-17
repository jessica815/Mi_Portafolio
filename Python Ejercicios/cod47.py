#Area y perimetro de un rombo sin nada, normalito
if __name__ == "__main__":
    D:float=float(input("Ingresa el valor de la diagonal mayor:  "))
    dm:float=float(input("Ingresa el valor de la diagonal menor: "))
    l:float=float(input("Ingresa el valor del lado: "))
    P:int=0
    area:int=0
    area=D*dm
    P=l+l+l+l
    print(f"Area= {area}")
    print(f"El perimetro es: {P}")