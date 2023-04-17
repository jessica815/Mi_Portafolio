#Area y circunferencia de un círculo sin nada, normalito
if __name__ == "__main__":
    pi:float=3.1416
    area:int=0
    cir:int=0
    r:float=float(input("Ingresa el valor de la radio:  "))
    if r>0:
        dia=r*2
        area=pi*r*r
        cir=pi*dia
        print(f"Area: {area}")
        print(f"La circunferencia es: {cir}")
    else:
        print("Error")
        
