idade = int(input("Insira a sua idade: "))

if idade < 16:
    print("A pessoa não pode votar")
elif idade >= 16 and idade < 18:
    print("Voto Opcional")
elif idade >= 18:
    print("Voto Obrigatorio")
elif idade > 70:
    print("Voto Opcional")