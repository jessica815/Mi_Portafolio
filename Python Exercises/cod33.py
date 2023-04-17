#Obtenga x^y por medio de sumas sucesivas. Indicando cuantas
# veces se sumó con while

if __name__ == "__main__":
    x:int=int(input("Ingresa el valor de tu base: "))
    y:int=int(input("Ingresa el valor de la potencia: "))
    R:int=0
    while x>0:
        while y>0:
            R=x**y
            break
        else:
            R=x**y
            break
        break
    else:
        while y>0:
            R=x**y
            break
        else:
            R=x**y
    print(R)
