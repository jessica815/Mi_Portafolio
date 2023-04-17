#sumatoria xi  donde  i=1 con while
if __name__ == "__main__":
    x:int=int(input("Ingresa la base: "))
    n:int=int(input("Ingresa el total de datos: "))
    c:int=1
    i:int=1
    sum:int=0
    mult:int=1
    while x<=0:
        print("Error, ingresa otro")
        x:int=int(input("Ingresa la base: "))

    while n<=0:
        print("Error, ingresa otro")
        n:int=int(input("Ingresa el total de datos: "))

    while c<=n:
        mult=x*i
        sum=sum+mult
        i=i+1
        c=c+1
        print(sum)
