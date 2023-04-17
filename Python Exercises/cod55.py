#Area y Perimetro de un trapecio con while
if __name__ == "__main__":
    B:float=float(input("Ingresa el valor de la base mayor: "))
    while B<0:
        print("Error")
        B:float=float(input("Ingresa el valor de la base mayor: "))

    bm:float=float(input("Ingresa el valor de la base menor: "))
    while bm<0:
        print("Error")
        bm:float=float(input("Ingresa el valor de la base menor: "))

    h:float=float(input("Ingresa el valor de la altura: "))
    while h<0:
        print("Error")
        h:float=float(input("Ingresa el valor de la altura: "))

    l:float=float(input("Ingresa el valor del lado: "))
    while l<0:
        print("Error")
        l:float=float(input("Ingresa el valor del lado: "))

    area:int=0
    P:int=0
    while B>0:
        while B>bm:
            area=h*B*bm/2
            P=B+bm+l+l
            break
        else:
            area=h*B*bm/2
            P=B+bm+l+l
            break
        break
    else:
        while bm>0:
            area=h*B*bm/2
            P=B+bm+l+l
            break
        else:
            while l>0:
                area=h*B*bm/2
                P=B+bm+l+l
                break
            else:
                while h>0:
                    area=h*B*bm/2
                    P=B+bm+l+l
                    break
                else:
                    area=h*B*bm/2
                    P=B+bm+l+l
    print(f"El área es: {area}")
    print(f"El perimetro es: {P}")