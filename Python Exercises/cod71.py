#Sucesion 3,8.13.18.23.28.33.38.... con for
if __name__ == "__main__":
    T:int=int(input("¿Hasta que número quieres llegar?: "))
    c:int=0
    if T>0:
        for i in range(3,T*5,5):
            print(f"{i}, ", end="")
            c=c+1
            if c==T:
                break
    else:
        while True:    
            T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
            if T>0:
                for i in range(3,T*5,5):
                    print(f"{i}, ", end="")
                    c=c+1
                if c==T:
                    break
                break
            else:
                print("Error, ingresa otro ")
            for i in range(3,T*5,5):
                print(f"{i}, ", end="")
                c=c+1
                if c==T:
                    break