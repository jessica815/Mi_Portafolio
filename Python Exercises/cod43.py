#Area y Perimetro de un rectangulo con while
if __name__ == "__main__":
    b:int=int(input("Ingresa el valor de la base: "))
    while b<0:
        print("Error")
        b:int=int(input("Ingresa el valor de la base: "))

    h:int=int(input("Ingresa el valor de la altura: "))
    while h<0:
        print("Error")
        h:int=int(input("Ingresa el valor de la altura: "))
        
    area:int=0
    P:int=0
    while b>0:
        while h>0:
            area=b*h
            P=b+b+h+h
            break
        else:
            area=b*h
            P=b+b+h+h
            break
        break
    else:
        while h>0:
            area=b*h
            P=b+b+h+h
            break
        else:
            area=b*h
            P=b+b+h+h
    print(f"El área es: {area}")
    print(f"El perimetro es: {P}")