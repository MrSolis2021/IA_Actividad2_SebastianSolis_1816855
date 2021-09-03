print("Hello world")

"Ejercicio 2"

"Instrucciones: Crear un programa que le pida al usuario capturar dos numeros enteros y dos" \
"numeros flotantes. Despues, realizara la suma, resta, multiplicacion y division de ambos pares" \
"de numero. Como resultado se deberan obtener 8 valores."

print("A continuacion deberas capturar dos numeros enteros.")
num_ent1 = int(input("Captura un numero entero: "))
num_ent2 = int(input("Captura otro numero entero: "))

print("Ahora deberas capturar dos numeros flotantes.\nRecuerda que los numeros flotantes son "
      "aquellos que cuentan con parte decimal.")
num_f1 = float(input("Ingresa un numero flotante: "))
num_f2 = float(input("Ingresa un segundo numero flotante: "))

print("Suma, resta, multiplicacion y division de numeros enteros, respectivamente: ")

print(num_ent1 + num_ent2)
print(num_ent1 - num_ent2)
print(num_ent1 * num_ent2)
print(num_ent1 / num_ent2)

print("Suma, resta, multiplicacion y division de numeros flotantes, respectivamente: ")
print(num_f1 + num_f2)
print(num_f1 - num_f2)
print(num_f1 * num_f2)
print(num_f1 / num_f2)
