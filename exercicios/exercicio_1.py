#Criar um programa que solicita ao usuário 6 números, calculando
#sua média. Mostrar ao usuário uma lista com os números iguais
#ou acima da média e uma lista com os números abaixo da média. 
numero_acima_media = []
numero_abaixo_media = []
numeros = []
for i in range(6):
    num = int(input(f"Digite o {i+1} numero:"))
    numeros.append(num)
    if num >= 6:
        numero_acima_media.append(num)
    else: 
        numero_abaixo_media.append(num)

print(f"os numeros acima da media são{numero_acima_media}")
print(f"os numeros abaixo da media são{numero_abaixo_media}")
print(f" os numeros são {numeros}")

media = sum(numeros)/len(numeros)
print(media)

    