# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
# la <n> entre <m> da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = input('Numerador entero: ')
m = input('Denominador entero: ')
n = int(n)
m = int(m)
c = n//m
r = n%m

print(f'Resultado: {c}\nResiduo: {r}')
