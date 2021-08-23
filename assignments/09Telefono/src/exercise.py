def main():
    #escribe tu código abajo de esta línea
    men=int(input(" Dame el número de mensajes: "))
    meg=float(input("Dame el número de megas: "))
    nmi=int(input("Dame el número de minutos: "))
    qmen=men*0.8
    qmeg=meg*0.8
    qnmi=nmi*0.8
    cm=qmen+qmeg+qnmi
    cm=round(cm,2)
    print("El costo mensual es: ",cm)
    pass

if __name__ == '__main__':
    main()

