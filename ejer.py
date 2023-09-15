# ClaudiaRamos-python
"""Encontrar el perimetro de un cuadrado"""
lado=int(input("Ingrese un número= "))

perimetro=4*lado

print(f'El perimetro de un cuadrado de lado {lado} es igual a: {perimetro}')

"""Encontrar el minimo y maximo de una lista de numeros"""

lista=[23,17,18,10,13,12,28,64,58,29]

maximo=max(lista)

minimo=min(lista)

print(f"Dela siguiente lista {lista} El maximo es {maximo} y el minimo es {minimo}")

"""Verificar si una cadena de texto contiene solo digítos"""

cadena=input("Escribe una caneda de digitos: ")

if cadena.isdigit():
    print(f"la cadena {cadena} contiene solo digitos")
else:
    print(f"la cadena {cadena} no contiene solo dígitos")
"""Calcular el factorial de un número utilizando una función recursiva"""

factorial=int(input("Escribe un número para sacar el factorial: "))  
a=1  
for x in range(1,factorial + 1):
    a=x*a
print(f"El factorial es:{a}")

"""Invertir una lista"""

lista=[1,2,3,4,5,6,7]
lista.reverse()
print(f"Tu lista invertida es:{lista}")
