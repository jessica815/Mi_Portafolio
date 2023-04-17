
#Sucesion 0,1,0,1,0,1.... con for
if __name__ == "__main__":
    c:int=0
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    if T>0:
        for i in range(0,T):
            if c%2==0:
                print("0,",end="")
            if c%2==1:
                print("1,",end="")
            c=c+1
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                break
            else:
                print("Error, ingresa otro ")
            for i in range(0,T):
                if c%2==0:
                    print("0,",end="")
                if c%2==1:
                    print("1,",end="")
                c=c+1
                if c==T:
                    break