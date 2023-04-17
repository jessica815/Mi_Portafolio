#Capture n números positivos y determine el promedio de ellos, 
# pueden ser positivos con while

if __name__ == "__main__":
    T:int=int(input("¿Cuántos números quieres ingresar?: "))
    n:int=int
    sum:int=0
    c:int=0
    while T<0:
        T:int=int(input("¿Cuántos números quieres ingresar?: "))
    while c<T:
        n:int=int(input("Ingresa un número: "))
        if n>0:
            sum = sum + n
            c=c+1
    print(f"Promedio: {sum/T}")