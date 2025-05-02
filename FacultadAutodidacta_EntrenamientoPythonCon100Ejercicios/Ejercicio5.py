"""Multiplicar una cadena por una número entero"""

Cadena = "-jamón del bueno-"
Cadena2 = "rar"
numero1 = 5
numero2 = 5
multiplicacion1 = numero1 * numero2
multiplicacion2 = multiplicacion1 * Cadena
ListaComida = ["Haba", "CocaCola", 5, "Patata"]

print("Multiplicación de la frase: ", multiplicacion2)

"""Dividir una cadena"""

CadenaDividida = Cadena.split()
print("División de la frase: ", CadenaDividida)


"""Tenemos un palíndromo?"""
palindr = Cadena == Cadena[::-1]
palindr2 = Cadena2 == Cadena2[::-1]
print("¿Palídromo?")
print("La frase: ", palindr)
print("La palabra rar: ", palindr2)

"""Borrar un objeto de la lista"""
ListaComida.remove(5)
print("Solo se ven cosas comestibles: ", ListaComida)

"""Generar números del 1 al 100"""
numeros = list(range(1, 201))
print("Números del 1 al 100")
print(numeros)
