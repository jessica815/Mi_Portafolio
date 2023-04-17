#Area y perimetro de un triangulo sin nada, normalito
if __name__ == "__main__":
    b:int=int(input("Ingresa el valor de base:  "))
    h:int=int(input("Ingresa el valor de la altura: "))
    P:int=0
    area:int=0
    area=b*h/2
    P=b+b+h+h
    print(f"Area= {area}")
    print(f"El perimetro es= {P}")