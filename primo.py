
x=int(input("Por favor, ingrese un número: "))


def numero_primo(x):
    for i in range (2,x+1):

     if (x%i)==0:
        print("Es primo")

    else:
      print("No es primo")

numero_primo(x)