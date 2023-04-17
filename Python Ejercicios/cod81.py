#sucesion 1,4,9,16,25,36,49,64... con while

if __name__ == "__main__":
    c:int=1
    x:int=0
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))

    while c<T:
        x=c**2        
        print(f"{x}, ", end="")
        c=c+1
        