#Area y Perimetro de un cuadrado con do-while
if __name__ == "__main__":
    l:int=int
    P:int=0
    area:int=0
    while True:
        l:int=int(input("Ingresa el valor del lado: "))
        if l>0:
            break
    area=l*l
    P=l+l+l+l
    print(f"El área es: {area}")
    print(f"El perimetro es: {P}")
