#Area y perimetro de un trapecio con do-while
if __name__ == "__main__":
    B:float=float
    bm:float=float
    h:float=float
    l:float=float
    area:int=0
    P:int=0
    while True:
        B:float=float(input("Ingresa el valor de la base mayor: "))
        if B>0:
            break
    while True:
        bm:float=float(input("Ingresa el valor de la base menor: "))
        if bm>0:
            break
    while True:
        h:float=float(input("Ingresa el valor de la altura: "))
        if h>0:
            break
    while True:
        l:float=float(input("Ingresa el valor del lado: "))
        if l>0:
            break
    area=h*B*bm/2
    P=B+bm+l+l
    print(f"El area es: {area}")
    print(f"El perimetro es: {P}")