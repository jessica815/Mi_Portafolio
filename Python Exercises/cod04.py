#Captura el nombre completo de una persona e imprimalo empezando por los apellidos y al final el nombre

if __name__ == "__main__":
    ap:str = str(input("Escribe tu apellido paterno: "))
    ap_m:str = str(input("Escribe tu apellido materno: "))
    nom:str = str(input("Escribe tu nombre: "))
    print (f"Hola {ap} {ap_m} {nom}")