#sucesion 3,9,27,81,243,729,2187,... con for

if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=3
    if T>0:
        for i in range(0,T):
            print(f"{c}, ", end="")
            c=c*3
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(0,T):
                    print(f"{c}, ", end="")
                    c=c*3
                if c==T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(0,T):
                print(f"{c}, ", end="")
                c=c*3
                if c==T:
                    break