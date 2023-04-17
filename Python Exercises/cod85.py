#sucesion 1,8,27,64,125,216,343,512,... con do-while

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
        x=c**3
        print(f"{x}, ", end="")
        c=c+1
        if c>=T:
            break