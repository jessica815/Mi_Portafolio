#sucesion 1,4,7,10,13,16,19,22,25 con do-while
if __name__ == "__main__":
    c:int=0
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")        
    for i in range(1,T*3,3):
        print(f"{i}, ", end="")