#sucesion 0,1,1,2,3,5,8,13,21,34,... con for

if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=0
    x:int=0
    y:int=1
    if T>0:
        for i in range(0,T):
            print(f"{x}, ", end="")
            x=x+1
            x=x+y-1
            c=c+1
            print(f"{y}, ", end="")
            y=y+x
            c=c+1
            if c>=T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(0,T):
                    print(f"{x}, ", end="")
                    x=x+1
                    x=x+y-1
                    c=c+1
                    print(f"{y}, ", end="")
                    y=y+x
                    c=c+1
                if c>=T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(0,T):
                print(f"{x}, ", end="")
                x=x+1
                x=x+y-1
                c=c+1
                print(f"{y}, ", end="")
                y=y+x
                c=c+1
            if c>=T:
                break
