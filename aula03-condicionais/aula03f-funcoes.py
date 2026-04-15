# FUNÇÃO COM PARAM
def boas_vindas(nome):
    print(f'Olá {nome}!! Seja bem vindo!!')

nome_indicado = input("Digite seu nome: ")
boas_vindas(nome_indicado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(7, 4)
print(resultado)

def pode_aprovar(idade):
    if idade >= 18:
        return True
    else:
        return False

if pode_aprovar(18):
    print("maior que 18")
