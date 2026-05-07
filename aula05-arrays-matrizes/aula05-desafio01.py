nomes = ["Rafael","David","Victor Roque", "Flaco Lopes"]
for nome1 in range(len(nomes)):
    for nome2 in range(nome1+1, len(nomes)):
        print(f"{nomes[nome1]} e {nomes[nome2]}")
