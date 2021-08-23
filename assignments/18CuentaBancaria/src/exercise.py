def main():
    #escribe tu código abajo de esta línea
    sal=float(input("Dame el saldo del mes anterior:"))
    ing=float(input("Dame los ingresos: "))
    egr=float(input("Dame los egresos: "))
    che=int(input("Dame el número de cheques: "))
    extendido=che*13
    total=((sal+ing-egr-extendido)*92.5)/100
    print("El saldo final de la cuenta es: ",total)
    pass

if __name__ == '__main__':
    main()

