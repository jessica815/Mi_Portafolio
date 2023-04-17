#Sucesion 1,4,7,10,13,15,19,22,25.... con for
if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=0
    if T>0:
        for i in range(1,T*3,3):
            print(f"{i}, ", end="")
            c=c+1
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(1,T*3,3):
                    print(f"{i}, ", end="")
                    c=c+1
                if c==T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(1,T*3,3):
                print(f"{i}, ", end="")
                c=c+1
                if c==T:
                    break