par = 0
impar = 0 
positivo = 0 
negativo = 0
print ("Digite 0 para encerrar o programa")
for i in range (1, 6 + 1):
    numero = int(input("Digite um número inteiro: "))
    if numero > 0 and i % 2 == 0:
        par += 1
        positivo += 1
    elif numero > 0 and i % 2 != 0:
        impar += 1
        positivo += 1
    elif numero < 0 and i % 2 == 0:
        par += 1
        negativo += 1
    else:
        impar += 1
        negativo += 1

    if numero == 0:
        break
    soma = positivo + positivo

print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")
print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Soma dos números positivos: {soma}")