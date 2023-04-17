#sucesion 0,1,1,2,3,5,8,13,21,34,... con while

if __name__ == "__main__":
    c:int=0
    x:int=0
    y:int=1
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<0:
        print("Error, ingresa otro")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))

    while c>=T:
        print(f"{x}, ", end="")
        x=x+1
        x=x+y-1
        c=c+1  
        print(f"{y}, ", end="")
        y=y+x
        c=c+1