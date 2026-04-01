# LÓGICA E (and)
# é a lógica do login
# email e a senha sejam True

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

# LÓGICA OU (or)
# SOL NO DOM    JOGO br         CHURRAS NO DOM
#False          TRUE            TRUE

logica_ou = False or False or False
print(logica_ou)

negacao = not True
print(negacao)

if not verifica_login:
    print("acerta ai...")