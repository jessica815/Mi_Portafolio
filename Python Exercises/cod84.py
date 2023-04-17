#sucesion 1,8,27,64,125,216,343,512,... con while

if __name__ == "__main__":
    c:int=1
    x:int=0
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))

    while c<T:
        x=c**3        
        print(f"{x}, ", end="")
        c=c+1