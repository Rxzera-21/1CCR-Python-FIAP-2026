lista_frutas = ["Banana", "Morango", "Manga"]
lista_frutas.append(input("Digite uma fruta que voce gosta: "))
print(lista_frutas[-1])

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

for fruta in lista_frutas:
    print(fruta)