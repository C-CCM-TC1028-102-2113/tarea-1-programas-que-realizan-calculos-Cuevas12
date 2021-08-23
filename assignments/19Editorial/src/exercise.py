def main():
    #escribe tu código abajo de esta línea
    import math
    numpag=int(input("Dame el número de palabras: "))
    paginas=(math.ceil(numpag/475))
    costo=(((paginas*60))*.90)
    print("El costo de la publicación es: ",costo)
    pass

if __name__ == '__main__':
    main()
