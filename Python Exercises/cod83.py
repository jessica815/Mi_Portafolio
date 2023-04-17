#sucesion 1,4,9,16,25,36,49,64... con for

if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=1
    x:int=0
    if T>0:
        for i in range(1,T):
            x=c**2
            print(f"{x}, ", end="")
            c=c+1
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(1,T):
                    x=c**2
                    print(f"{x}, ", end="")
                    c=c+1
                if c==T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(1,T):
                print(f"{c}, ", end="")
                x=c**2
                c=c+1
                if c<=T:
                    break