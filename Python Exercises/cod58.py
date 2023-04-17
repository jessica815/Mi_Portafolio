#Area y circunferencia de un círculo con while
if __name__ == "__main__":
    rad:float=float(input("Ingresa el valor del radio: "))
    while rad<0:
        print("Error")
        rad:float=float(input("Ingresa el valor del radio: "))

    area:int=0
    cir:int=0
    pi:float=3.1416
    while rad>0:
        while rad>0:
            dia=rad*2
            area=pi*rad*rad
            cir=pi*dia
            break
        else:
            dia=rad*2
            area=pi*rad*rad
            cir=pi*dia
            break
        break
    else:
        dia=rad*2
        area=pi*rad*rad
        cir=pi*dia
    print(f"El área es: {area}")
    print(f"El perimetro es: {cir}")