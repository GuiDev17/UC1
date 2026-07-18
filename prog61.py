def montar_carrinho():
    #1-> Criamos a lista vazia( o carrinho)
    carrinho=[]

    print("==BEM-VINDO AO SUPERMERCADO PYTHON ===")

    #2-> Laço de repetição para capturar múltiplos itens
    while True:
        produto= input("Digite um produto (ou digite 'sair'): ")

        #Se o usuario quiser sair, interrompemos o laço
        if produto.lower() == 'sair':
            break

        #3-> Adiciona o produto digitado ao final da lista
        carrinho.append(produto)
        print(f"-->'{produto} adicionado ao carrinho com sucesso!\n")

        #4-> Exibe o resultado final
    print("\n=== SEU CARRINHO DE COMPRAS ===")
    if len(carrinho) == 0:
        print("SEu carrinho esta vazio.")
    else:
        #Exibe os intens um embaixo do outro
        for item in carrinho:
            print(f"-{item}")

    print(f"\nTotal de itens no carrinho: {len(carrinho)}")

#Testando a funçao:
montar_carrinho() 