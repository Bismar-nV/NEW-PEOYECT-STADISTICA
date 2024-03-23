import math

def calcular_precision(valor):
    if isinstance(valor, (int, float)):
        if int(valor) == valor:
            return 1
        elif round(valor, 1) == valor:
            return 0.1
        elif round(valor, 2) == valor:
            return 0.01
        elif round(valor, 3) == valor:
            return 0.001
        # Puedes seguir agregando más casos según la precisión necesaria
    else:
        return "No es un número"


# Datos
datos = [
    26, 32, 30, 27, 37, 37, 36, 28, 28, 31,
    28, 33, 31, 35, 34, 26, 27, 33, 30, 26,
    29, 28, 30, 26, 37, 36, 38, 27, 33, 30
]
# Número de datos
numero_datos = len(datos)

# Alcance (min y longitud)
min_valor = min(datos)
max_valor = max(datos)

precision = calcular_precision(max_valor)
longitud_alcance = max_valor - min_valor + precision  # Aquí corregimos el cálculo

# Número de intervalos
numero_intervalos = 1 + 3.3 * math.log10(numero_datos)
numero_intervalos_redondeado = round(numero_intervalos)

# Tamaño de clase
tamanio_clase = longitud_alcance / numero_intervalos_redondeado
tamanio_clase_redondeado = math.ceil(tamanio_clase)  # Redondeamos hacia arriba

# Arreglo de clase
areglo = numero_intervalos_redondeado * tamanio_clase_redondeado

# Diferencia de longitud con el arreglo redondeado
diferencia_longitud_arreglo = areglo - longitud_alcance
# Particionamiento de la diferencia en dos números
num1 = math.ceil(diferencia_longitud_arreglo / 2)
num2 = diferencia_longitud_arreglo - num1

# Sumar el número mayor al valor máximo
nuevo_maximo = max_valor + num1

# Restar el número menor al valor mínimo
nuevo_minimmo = min_valor - num2

# Mostrar resultados
print("Número de datos:", numero_datos)
print("Valor mínimo:", min_valor)
print("Valor máximo:", max_valor)
print("Longitud del alcance:", longitud_alcance)
print("Número de intervalos:", numero_intervalos_redondeado)
print("Tamaño de clase:", tamanio_clase_redondeado)
print("Arreglo de clase:", areglo)
print("Diferencia de longitud con el arreglo redondeado:", diferencia_longitud_arreglo)
print("Particionamiento de la diferencia en dos números:", num1, num2)
print("Nuevo mínimo:", nuevo_maximo)
print("Nuevo máximo:", nuevo_minimmo)


# Definir intervalos
intervalos = [(24, 27), (27, 30), (30, 33), (33, 36), (36, 39)]

# Calcular frecuencia absoluta para cada intervalo
fi_1 = []
for intervalo in intervalos:
    min_intervalo, max_intervalo = intervalo
    fi_1.append(sum(1 for dato in datos if min_intervalo <= dato < max_intervalo))

# Imprimir frecuencia absoluta para cada intervalo
#for i, intervalo in enumerate(intervalos):
#   print(f"Intervalo {intervalo}: {fi_1[i]}")
total_datos = sum(fi_1)

# Calcular hi_1 (frecuencia relativa)
hi_1 = [f / total_datos for f in fi_1]

# Calcular pi_1 (frecuencia relativa porcentual)
pi_1 = [round(h * 100, 2) for h in hi_1]

# Calcular Fi_1 (frecuencia absoluta acumulada)
Fi_1 = [sum(fi_1[:i+1]) for i in range(len(fi_1))]

# Calcular Hi_1 (frecuencia relativa acumulada)
Hi_1 = [round(F / total_datos, 4) for F in Fi_1]

# Calcular Pi_1 (frecuencia relativa acumulada porcentual)
Pi_1 = [round(H * 100, 2) for H in Hi_1]

# Imprimir la tabla
print("| Intervalos | Fi 1 |  hi 1 |  pi 1 |  Fi 1 |  Hi 1 |  Pi 1 |")
print("|------------|------|-------|-------|-------|-------|-------|")
for i in range(len(intervalos)):
    print(f"| {str(intervalos[i]):^11} | {fi_1[i]:^4} | {hi_1[i]:^6.4f} | {pi_1[i]:^6.2f} | {Fi_1[i]:^5} | {Hi_1[i]:^6.4f} | {Pi_1[i]:^6.2f} |")

