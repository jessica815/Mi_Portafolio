#sucesion 1,4,9,16,25,36,49,64... con do-while

if __name__ == "__main__":
    c:int=1
    x:int=0
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")        
    while True:
        x=c**2
        print(f"{x}, ", end="")
        c=c+1
        if c>=T:
            break