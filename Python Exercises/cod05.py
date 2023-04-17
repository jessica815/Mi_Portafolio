#Imprime la edad de una persona de acuerdo a su año de nacimiento

if __name__ == "__main__":
    a_nac:int = int(input("¿Año de nacimiento?: "))
    act:int = int(input("¿Año actual?: "))
    edad= act-a_nac
    print(f"Tu edad es: {edad}")