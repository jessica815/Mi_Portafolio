#sucesion 1,4,7,10,13,16 con while
if __name__ == "__main__":
    c:int=0
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro ")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    for i in range(1,T*3,3):
        print(f"{i}, ", end="")