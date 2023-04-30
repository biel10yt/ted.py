# vetor vazio de 20 elementos
numeros = [0] * 20

# Lê os 20 números e armazena no vetor
for i in range(20):
    numeros[i] = int(input("Digite um número: "))

# ordem inversa
for i in range(19, -1, -1):
    print(numeros[i])
