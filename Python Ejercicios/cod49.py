#Area y perimetro de un rombo con while
if __name__ == "__main__":
    D:float=float(input("Ingresa el valor de la diagonal mayor: "))
    while D<=0:
        print("Error")
        D:float=float(input("Ingresa el valor de la diagonal mayor: "))
    dm:float=float(input("Ingresa el valor de la diagonal menor: "))
    while dm<=0:
        print("Error")
        dm:float=float(input("Ingresa el valor de la diagonal menor: "))
    l:float=float(input("Ingresa el valor del lado: "))
    while l<=0:
        print("Error")
        l:float=float(input("Ingresa el valor del lado: "))

    area:int=0
    P:int=0
    while D>0:
        while D>dm:
            area=D*dm
            P=l+l+l+l
            break
        else:
            area=D*dm
            P=l+l+l+l
            break
        break
    else:
        while dm>0:
            area=D*dm
            P=l+l+l+l
            break
        else:
            while l>0:
                area=D*dm
                P=l+l+l+l
                break
            else:
                area=D*dm
                P=l+l+l+l
    print(f"El área es: {area}")
    print(f"El perimetro es: {P}")