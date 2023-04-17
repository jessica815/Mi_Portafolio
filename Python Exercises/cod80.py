#sucesion 1,3,6,10,15,21,28,36... con for

if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=0
    x:int=1
    if T>0:
        for i in range(2,T+2):
            print(f"{x}, ", end="")
            x=x+i
            c=c+1
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(2,T+2):
                    print(f"{x}, ", end="")
                    x=x+i
                    c=c+1
                if c==T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(2,T+2):
                print(f"{c}, ", end="")
                x=x+i
                c=c+1
                if c<=T:
                    break