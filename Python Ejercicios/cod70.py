#sucesion 3,8,13,18,23,28,33,38... con do-while
if __name__ == "__main__":
    c:int=0
    while True:    
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
        if T>0:
            break
        else:
            print("Error, ingresa otro ")        
    for i in range(3,T*5,5):
        print(f"{i}, ", end="")