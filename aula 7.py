 # dicionário: nome -> preço
precos = {}
for produto in vitrine:
    precos[produto["nome"]] = produto["preco"]

    total = 0
    for nome, quantidade in carrinho:
     total = total + precos[nome] * quantidade
    print("Peças na vitrine:", len(vitrine))
    print("Total do carrinho: R$", round(total, 2))


    print(vitrine[1]["preco"])
print(TAMANHOS[-1])
print(len(carrinho))
print(precos["Moletom"] * 2) 


python-vitrine.py
Peças_navitrine: 3
Total_do_carrinho: 