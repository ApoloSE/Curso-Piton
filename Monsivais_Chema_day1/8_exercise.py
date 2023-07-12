# Una panadería vende barras de pan a 3.49 MXN cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


n = input('Barras de pan vendidas: ')
n = int(n)
off = (3.49*0.4)*n
price = (3.49*n)-off
print(f'Precio Nomal de unidad: ${3.49}\nDescuento total: ${round((off),2)}\nCoste total: ${round((price),2)}')