#sucesion 3,9,27,81,243,729,2187,... con while

if __name__ == "__main__":
    c:int=3
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro ")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    for i in range(0,T):
        print(f"{c}, ", end="")
        c=c*3