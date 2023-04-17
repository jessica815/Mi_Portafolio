#Capture n números positivos y determine el promedio de ellos, 
# pueden ser positivos o negativos con do-while
if __name__ == "__main__":
    while True:
        T:int=int(input("¿Cuántos números quieres ingresar?: "))
        if T > 0:
            break 
    sum:int=0  
    for i in range(T): 
        while True:
            n:int = int(input(f"Ingresa un número {i+1}: "))
            if n>0:
                break
            else:
                print("Error") 
    
        sum = sum + n
    print(f"Promedio: {sum/T}")