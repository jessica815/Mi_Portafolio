#sucesion 2,4,8,16,32,64,128,256... con while
if __name__ == "__main__":
    c:int=2
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro ")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    for i in range(0,T):
        print(f"{c}, ", end="")
        c=c*2