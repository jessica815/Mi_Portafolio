#sucesion 1,3,6,10,15,21,28,36... con do-while

if __name__ == "__main__":
    c:int=0
    x:int=1
    sum1:int=2
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")        
    while True:
        print(f"{x}, ", end="")
        x=x+sum1
        sum1=sum1+1
        c=c+1
        if c>=T:
            break
    
            