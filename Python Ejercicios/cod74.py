#sucesion 2,4,8,16,32,64,128,256... con for


if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=2
    if T>0:
        for i in range(0,T):
            print(f"{c}, ", end="")
            c=c*2
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(0,T):
                    print(f"{c}, ", end="")
                    c=c*2
                if c==T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(0,T):
                print(f"{c}, ", end="")
                c=c*2
                if c==T:
                    break