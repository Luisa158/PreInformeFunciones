
def potencia_numero():
    x1=int(input("Por favor, introduzca el número base: "))
    a=int(input("Por favor, introduzca la potencia: "))

    x2= int(input("Por favor, introduzca el número base: "))
    b= int(input("Por favor, introduzca la potencia: "))

    res1=x1**a
    res2=x2**b

    if res1>res2:
        print("El número mayor es: ", res1)

    else:
        print("El número mayor es: ", res2)
potencia_numero()



