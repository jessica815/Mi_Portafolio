#Area y Perimetro de un cuadrado con while
if __name__ == "__main__":
    l:int=int
    area:int=0
    P:int=0
    l:int=int(input("Ingresa el valor del lado: "))
    while l>0:
        area=l*l
        P=l+l+l+l
        print(f"El área es: {area}")
        print(f"El perimetro es: {P}")
        break
    else:
        while True:
            print("No válido")
            l:int=int(input("Ingresa el valor del lado: "))
            if l>0:
                break
        area=l*l
        P=l+l+l+l
        print(f"El área es: {area}")
        print(f"El perimetro es: {P}")