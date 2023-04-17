#Area y perimetro de un trapecio sin nada, normalito
if __name__ == "__main__":
    B:float=float(input("Ingresa el valor de base mayor:  "))
    bm:float=float(input("Ingresa el valor de base menor:  "))
    h:float=float(input("Ingresa el valor de la altura: "))
    l:float=float(input("Ingresa el valor del lado: "))
    P:int=0
    area:int=0
    if B<0:
        print("Error")
        B:float=float(input("Ingresa el valor de base mayor:  "))
    if bm<0:
        print("Error")
        bm:float=float(input("Ingresa el valor de base menor:  "))
    if h<0:
        print("Error")
        h:float=float(input("Ingresa el valor de la altura: "))
    if l<0:
        print("Error")
        l:float=float(input("Ingresa el valor del lado: "))

    area=h*B*bm/2
    P=B+bm+l+l
    print(f"Area= {area}")
    print(f"El perimetro es= {P}")