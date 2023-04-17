#sucesion 0,1,0,1,0,1,0 con do-while

if __name__ == "__main__":
    c:int=0
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")
    while True:
        if c%2==0:
            print("0,",end="")
        if c%2==1:
            print("1,",end="")
        c=c+1
        if c==T:
            break
