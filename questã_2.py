# Inicializa um vetor vazio com 10 elementos
vet = [0] * 10

# Lê os 10 números e armazena no vetor
for i in range(10):
    vet[i] = int(input("Digite um número: "))

# Verifica se existem números repetidos e suas posições
repetidos = []
for i in range(len(vet)):
    for j in range(i+1, len(vet)):
        if vet[i] == vet[j]:
            if vet[i] not in repetidos:
                repetidos.append(vet[i])
            print(f"Os números {vet[i]} se repetem nas posições {i} e {j}")

# Escreve os números repetidos e suas posições
if len(repetidos) == 0:
    print("Não há números repetidos no vetor.")
else:
    print(f"Os números repetidos são: {repetidos}")
