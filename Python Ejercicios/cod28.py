#Adivina el número secreto que cuando adivine le diga "Felicidades"
# y solo tenga 3 intentos e imprima "Te pasaste" o
# "Te falta" dependiendo el número introducido con do-while

if __name__ == "__main__":
    ns:int=5
    c:int=0
    while True:
        nums:int=int(input("Adivina el numero secreto: "))
        if nums==ns:
            print("Felicidades, ganaste")
            break
        else:
            c=c+1
            if nums>ns:
                print("Te pasaste")
                print(f"Llevas {c} intentos")
            if nums<ns:
                print("Te falta")
                print(f"Llevas {c} intentos")
        if c>=3:
            print("Perdiste")
            break