estoque = []

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Fruta
    2 - Excluir Fruta
    3 - Ver todas as Frutas
    0 - Sair do menu
"""))
    match menu:
        case 1:
            nome_fruta = str(input("Digite o nome da fruta: "))
            quantidade_fruta = str(input("Digite a quantidade de frutas no estoque: "))
            preco_fruta = str(input("Digite o preço da fruta: "))

            dicionario_fruta = {
                "Nome": nome_fruta,
                "Quantidade": quantidade_fruta,
                "Preço": preco_fruta
            }

            estoque.append(dicionario_fruta)
            print("Fruta adicionada com sucesso")
        case 2:
            for posicao,fruta in enumerate(estoque):
                print(f"""
                {posicao} -> {fruta["Nome"]}
""")

            posicao_excluida = int(input("Digite o número da fruta que você quer deletar: "))
            if posicao_excluida >= 0 and posicao_excluida < len(estoque):
                estoque.pop(posicao_excluida)
                print("Fruta excluída com sucesso")
            else:
                print("Meu fiiiii, digite uma posição dentro da lista que eu mostrei")
        
        case 3:
            for i ,fruta in enumerate(estoque):
                print(f"{i+1} - {fruta}")
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida")