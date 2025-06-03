# Ejercicio 1: Suma de dos números
print("\n--- Ejercicio 1: Suma de dos números ---")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("La suma es:", a + b)

# Ejercicio 2: Conversión de grados Celsius a Fahrenheit
print("\n--- Ejercicio 2: Conversión de Celsius a Fahrenheit ---")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius * 1.8 + 32
print("Temperatura en Fahrenheit:", fahrenheit)

# Ejercicio 3: Área de un triángulo
print("\n--- Ejercicio 3: Área de un triángulo ---")
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)

# Ejercicio 4: Par o impar
print("\n--- Ejercicio 4: Par o impar ---")
numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 5: Intercambiar valores sin variable auxiliar
print("\n--- Ejercicio 5: Intercambiar valores ---")
x = input("Valor de x: ")
y = input("Valor de y: ")
print("Antes: x =", x, ", y =", y)
x, y = y, x
print("Después: x =", x, ", y =", y)

# Ejercicio 6: Calculadora simple
print("\n--- Ejercicio 6: Calculadora simple ---")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
if num2 != 0:
    print("División:", num1 / num2)
else:
    print("No se puede dividir por cero.")

# Ejercicio 7: Edad en años, meses y días
print("\n--- Ejercicio 7: Edad en años, meses y días ---")
edad_anios = int(input("¿Cuántos años tienes? "))
meses = edad_anios * 12
dias = edad_anios * 365
print("Tienes aproximadamente", meses, "meses y", dias, "días.")

# Ejercicio 8: Número mayor
print("\n--- Ejercicio 8: Número mayor ---")
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
mayor = max(n1, n2, n3)
print("El número mayor es:", mayor)

# Ejercicio 9: Verificar múltiplo
print("\n--- Ejercicio 9: Verificar múltiplo ---")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num2 != 0 and num1 % num2 == 0:
    print(num1, "es múltiplo de", num2)
else:
    print(num1, "no es múltiplo de", num2)

# Ejercicio 10: Salario con bonificación
print("\n--- Ejercicio 10: Salario con bonificación ---")
salario_base = float(input("Ingresa tu salario base: "))
bono = salario_base * 0.10
salario_total = salario_base + bono
print("Tu salario total con bonificación es:", salario_total)