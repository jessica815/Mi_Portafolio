#Area y Perimetro de un rectangulo normalito, sin nada
if __name__ == "__main__":
    b:int=int(input("Ingresa el valor de base:  "))
    h:int=int(input("Ingresa el valor de la altura: "))
    P:int=0
    area:int=0
    area=b*h
    P=b+b+h+h
    print(f"Area= {area}")
    print(f"El perimetro es: {P}")