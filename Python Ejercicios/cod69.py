#sucesion 3,8,13,18,23,28,33,38... con while
if __name__ == "__main__":
    c:int=0
    T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    while T<=0:
        print("Error, ingresa otro ")
        T:int=int(input("¿Hasta que número quieres llegar en la sucesión?: "))
    for i in range(3,T*5,5):
        print(f"{i}, ", end="")

  