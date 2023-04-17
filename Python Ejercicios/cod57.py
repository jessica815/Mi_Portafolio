#Area y circunfereencia de un círculo con do-while
if __name__ == "__main__":
    rad:float=float
    pi:float=3.1416
    area:int=0
    cir:int=0
    while True:
        rad:float=float(input("Ingresa el valor del radio: "))
        if rad>0:
            break
    dia=rad*2
    area=pi*rad*rad
    cir=pi*dia
    print(f"El area es: {area}")
    print(f"La circunferencia es: {cir}")
