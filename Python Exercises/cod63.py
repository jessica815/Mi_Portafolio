#sucesion 0,1,0,1,0,1,0 con while
if __name__ == "__main__":
    c:int=0
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<0:
        print("Error, ingresa otro ")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while c<=T:
        if c%2==0:
            print("0, ", end="")
        if c%2==1:
            print("1, ", end="")
        c=c+1