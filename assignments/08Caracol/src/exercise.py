def main():
    #escribe tu código abajo de esta línea
    min=float(input("Dame los minutos: "))
    m_x_cm= min*5.7*6
    m_x_cm= round(m_x_cm,1)   
    print("Centímentros recorridos: "+str(m_x_cm))
    pass

if __name__ == '__main__':
    main()
