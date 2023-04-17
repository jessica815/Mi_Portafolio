#Area y Perimetro de u rectangulo con do-while
if __name__ == "__main__":
    b:int=int
    h:int=int
    area:int=0
    P:int=0
    while True:
        b:int=int(input("Ingresa el valor de la base: "))
        if b>0:
            break
    while True:
        h:int=int(input("Ingresa el valor de la altura: "))
        if h>0:
            break
    area=b*h
    P=b+b+h+h
    print(f"El area es: {area}")
    print(f"El perimetro es: {P}")