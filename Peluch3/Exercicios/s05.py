# Calcule os 5 primeiros multiplos > 0 

# Usando while para contagem regressiva

# Imprima um valor ate 100k

contador: int = 0
numero: float = 0
lista_numeros: list = [contador]

while contador <= 100:
    print(contador)
    print("Multiplos de 3")
    for numero in range(1, contador, 1):
        if numero % 3 == 0:
            print(numero)
        if numero % 2 == 1:
            lista_numeros.append(numero)
    contador += 10
print("FIM!")
print(f"Numeros primos: {lista_numeros}")
