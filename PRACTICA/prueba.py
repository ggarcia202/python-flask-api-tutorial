print("Flask API module")


# Funcion de impresion de valores y tipos de datos
def imprimir_valor_tipo(indice, valor, saludar=False): # indice y valor son parametros (argumentos), saludar es un parametro opcional con valor por defecto False
    print(f"{indice}. El valor es: {valor}, Tipo: {type(valor)}\n") # la f en el string permite usar variables dentro de {}
    if saludar is True:
        print("¡Hola! Este es un saludo desde la función imprimir_valor_tipo.\n\n")

    return # return vacio devuelve None


i=1
a = 3
imprimir_valor_tipo(i, a) # int (entero)
i += 1 # i = i + 1 


a = 4.5
imprimir_valor_tipo(i, a) # float (decimal)
i += 1


b = 3 # int
a = 4.5 # float
a = b + a # float
imprimir_valor_tipo(i, a)  # float (decimal)
i += 1


a = "Prueba"
i += 1
imprimir_valor_tipo(i, a) # str (string, cadena de texto)

a = "3"
i += 1
imprimir_valor_tipo(i, a) # str (string, cadena de texto)


b = "3"
a = "Prueba"
a = a + b # str se concatena (string, cadena de texto)
i += 1
imprimir_valor_tipo(i, a) # str (string, cadena de texto)

ha_ido_bien = True
try:
    b = 3
    a = "Prueba"
    a = a + b # ESTE DA ERROR: str no se puede sumar con int
    i += 1
    imprimir_valor_tipo(i, a)
except Exception as e: # Cualquier error se captura aquí da igual cual sea y me pertime continuar la ejecucion del programa
    ha_ido_bien = False
    i += 1
    print(f"{i}. Error al sumar str con int: {e}")

print(f"¿Ha ido bien hasta ahora? {ha_ido_bien}\n")

# Ejemplo de creación de una clase de error personalizada
class TypeErrorExample(Exception): # Crear una clase con herencia de Exception
    pass


a = "67"
try:
    a = int(a) # Casteo de str a int (entero)
    i += 1
    imprimir_valor_tipo(i, a) # int
except Exception as e:
    i += 1
    print(f"{i}. Error al castear str a int: {e}\n")


a = "67 años"
try:
    a = int(a) # Casteo de str a int (entero)
    i += 1
    imprimir_valor_tipo(i, a) # int
except Exception as e:
    i += 1
    print(f"{i}. Error al castear str a int: {e}\n")


   #0  1  2  3  4
a= [1, 2, 3, 4, 5]
i += 1
print(f"{i}. El valor de a es: {a}, Tipo de a: {type(a)}") # list (lista)
print(f"El segundo elemento de a es: {a[1]}")
print()


a= [1, 2, 3, 4, 5]
print(f"{i}. Lista a original: {a}")
# print("Longitud de la lista a:", len(a))
print(f"Longitud de la lista a: {len(a)}") # len() función que devuelve la longitud de una lista, viene de 'length' (longitud)
# Calculo la longitud a mano
longitud_a = 0
for elemento in a: # Para cada elemento en la lista a...
    longitud_a += 1 # Sumo 1 a la variable de longitud calculada a mano
print("Longitud de la lista a calculada a mano:", longitud_a, "\n")
i += 1


a= [1, 2, 3, 4, 5]
# a[0] += 0.5
# a[1] += 0.5
# a[2] += 0.5
# a[3] += 0.5
# a[4] += 0.5
d = 0.5
# a = [elemento + d for elemento in a]
# range(5) -> [0, 1, 2, 3, 4]
for j in range(len(a)): # range genera una secuencia de números desde 0 hasta el valor indicado -1 es decir 0 a 4 aqui
    print(f"\tÍndice {j}, Valor antes de sumar: {a[j]}")
    a[j] += d
imprimir_valor_tipo(i, a, saludar=True) # list (lista)



b = 5.67
c = "German"
a += [b] # Castea b a lista y lo añade al final a = a + [b]
a += [c] # Castea c a lista y lo añade al final
i += 1
print(f"El valor de a es: {a}, Tipo de a: {type(a)}") # list (lista)
print(f"El segundo elemento de a es: {a[1]}")
print()


a = {"Juan": 1, "Pedro": 2} # Ejemplo de diccionario
i += 1
print(f"{i}. El valor de a es: {a}, Tipo de a: {type(a)}")
print(f"Juan ha tardado: {a['Juan']}, y Pedro ha tardado: {a['Pedro']}")
print()


# Creame una lista de nombres comunes 
nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
valores = ["Peso", "Altura", "Edad", "Ciudad", "País"]


try:
    print("Pulsa Control+C para interrumpir el bucle")
    for i in range (10000000000):
        print(i, end="\r")
except KeyboardInterrupt:
    print("\nBucle interrumpido por el usuario")

#Agregar datos = append, insert, extend
#Eliminar datos = pop, remove, clear
#Buscar = index, count
#Reordenar = sort, reverse