
def primo_hermano():
    cont=0
    x=int(input("Por favor, ingrese un número: "))
    for i in range (1,100):
        if x%i==0:
            cont+=1
    if cont ==2:
        print("Es primo")
    elif x%6!=0:
        print("Es primo hermano")
    else:
        print("No es primo hermano")

primo_hermano()
