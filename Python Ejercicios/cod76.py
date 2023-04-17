#sucesion 3,9,27,81,243,729,2187,... con do-while
if __name__ == "__main__":
    c:int=3
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")        
    for i in range(0,T):
        print(f"{c}, ", end="")
        c=c*3
    