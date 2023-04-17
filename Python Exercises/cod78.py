#sucesion 1,3,6,10,15,21,28,36... con while
if __name__ == "__main__":
    c:int=0
    x:int=1
    sum1:int=2
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))

    while c<T:
        print(f"{x}, ", end="")
        x=x+sum1
        sum1=sum1+1
        c=c+1