#Adivina el número secreto que cuando adivine le diga "Felicidades"
# y solo tenga 3 intentos con for

if __name__ == "__main__":
    ns:int=5
    c:int=0
    for i in range(1,3+1):
        nums:int=int(input("Adivina el número secreto: "))
        if nums==ns:
            print("Felicidades, ganaste")
            break
        else:
            c=c+1
            print(f"Llevas {c} intentos")
        if c>=3:
            print("Perdiste")
            break
