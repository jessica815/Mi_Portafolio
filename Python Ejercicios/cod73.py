#sucesion 2,4,8,16,32,64,128,256... con do-while
if __name__ == "__main__":
    c:int=2
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")       
    for i in range(0,T):
        print(f"{c}, ", end="")
        c=c*2


