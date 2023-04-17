#Area y Perimetro de un pentagono con while
if __name__ == "__main__":
    lad:float=float(input("Ingresa el valor del lado: "))
    while lad<0:
        print("Error")
        lad:float=float(input("Ingresa el valor de lado: "))

    apo:float=float(input("Ingresa el valor del apotema: "))
    while apo<0:
        print("Error")
        apo:float=float(input("Ingresa el valor del apotema: "))

    area:int=0
    P:int=0
    while lad>0:
        while apo>0:
            P=lad+lad+lad+lad+lad
            area=P*apo
            break
        else:
            P=lad+lad+lad+lad+lad
            area=P*apo
            break
        break
    else:
        while apo>0:
            P=lad+lad+lad+lad+lad
            area=P*apo
            break
        else:
            P=lad+lad+lad+lad+lad
            area=P*apo
    print(f"El área es: {area}")
    print(f"El perimetro es: {P}")