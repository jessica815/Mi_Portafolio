#Area y Perimetro de un triángulo con while
if __name__ == "__main__":
    b:float=float(input("Ingresa el valor de la base: "))
    while b<0:
        print("Ingrese un valor mayor a 0")
        b:float=float(input("Ingresa el valor de la base: "))

    h:float=float(input("Ingresa el valor de la altura: "))
    while h<0:
        print("Ingresa un valor mayor a 0")
        h:float=float(input("Ingresa el valor de la altura: "))

    area:int=0
    P:int=0
    while b>0:
        while h>0:
            area=b*h/2
            P=b+b+h+h
            break
        else:
            area=b*h/2
            P=b+b+h+h
            break
        break
    else:
        while h>0:
            area=b*h/2
            P=b+b+h+h
            break
        else:
            area=b*h/2
            P=b+b+h+h
    print(f"El área es: {area}")
    print(f"El perimetro es: {P}")