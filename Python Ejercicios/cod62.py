
#Area y perimetro de un polígono regular de n lados, donde n está dentro del rango[5,12] sin nada, normalito
if __name__ == "__main__":
    fig:str=str(input("¿Qué figura realizarás?: "))
    lads:float=float(input("¿Cuántos lados tiene la figura?: "))
    apo:float=float(input("Ingresa el valor del apotema: "))
    n:float=float(input("¿Cuánto mide uno de los lados?: "))
    P:float=0
    area:float=0
    
    if lads < 5 or lads > 12:
        print("Error: el número de lados debe estar en el rango [5,12].")
    elif n <= 0:
        print("Error: la longitud del lado debe ser un número positivo.")
    elif apo <= 0:
        print("Error: el apotema debe ser un número positivo.")
    else:
        P = n * lads
        area = P * apo / 2
        print(f"El perimetro es {P}")
        print(f"El área es {area}")
