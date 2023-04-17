#En la FIME se desea obtener cuantos hombres y cuantas mujeres
#hay en cada una de las carreras (IM, IME, ICI, ISET, ISC) con do-while

if __name__ == "__main__":
    imh:int=0
    imm:int=0
    imeh:int=0
    imem:int=0
    icih:int=0
    icim:int=0
    iseth:int=0
    isetm:int=0
    isch:int=0
    iscm:int=0
    while True:
        opc:int=int(input("Elige la opción que deseas:\n 1.-IM\n 2.-IME\n 3.-ICI\n 4.-ISET\n 5.-ISC\n 6.-Terminar\n"))
        if opc==1:   
            sex:int=int(input("¿Sexo?:\n 1.-Hombre\n 2.-Mujer\n "))
            if sex==1:
                imh=imh+1
            elif sex==2:
                imm=imm+1
        elif opc==2:
            sex:int=int(input("¿Sexo?:\n 1.-Hombre\n 2.-Mujer\n "))
            if sex==1:
                imeh=imeh+1
            elif sex==2:
                imem=imem+1
        elif opc==3:
            sex:int=int(input("¿Sexo?:\n 1.-Hombre\n 2.-Mujer\n "))
            if sex==1:
                icih=icih+1
            elif sex==2:
                icim=icim+1
        elif opc==4:
            sex:int=int(input("¿Sexo?:\n 1.-Hombre\n 2.-Mujer\n "))
            if sex==1:
                iseth=iseth+1
            elif sex==2:
                isetm=isetm+1
        elif opc==5:
            sex:int=int(input("¿Sexo?:\n 1.-Hombre\n 2.-Mujer\n "))
            if sex==1:
                isch=isch+1
            elif sex==2:
                iscm=iscm+1
        elif opc==6:
            break
    print(f"IMhombres= {imh}\nIMmujeres= {imm}\nIMEhombres= {imeh}\nIMEmujeres= {imem}\nICIhombres= {icih}\nICImujeres= {icim}\nISEThombres= {iseth}\nISETmujeres= {isetm}\nISChombres= {isch}\nISCmujeres= {iscm}\n")
