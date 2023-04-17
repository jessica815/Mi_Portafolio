#Adivina el número secreto con 3 intentos con do-while

if __name__ == "__main__":
    c:int=0
    ns:int=5
    while True:
        nums:int=int(input("Adivina el numero secreto: "))
        if nums==ns:
            print("Felicidades, ganaste")
            break
        else:
            c=c+1
            print(f"Llevas {c} intentos")
        if c>=3:
            print("Perdiste")
            break
