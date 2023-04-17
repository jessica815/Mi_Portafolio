#Area y perimetro de un romboide sin nada, normalito
if __name__ == "__main__":
    b:float=float(input("Ingresa el valor de base:  "))
    h:float=float(input("Ingresa el valor de la altura: "))
    P:int=0
    area:int=0
    area=b*h
    P=b+b+h+h
    print(f"Area= {area}")
    print(f"El perimetro es= {P}")