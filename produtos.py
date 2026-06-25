# TUPLA -> Armazena categorias fixas que não serão alteradas
categorias = (
    "Romance",
    "Tecnologia",
    "História")

# LISTA -> Armazena todos os produtos cadastrados no sistema
estoque = []


# WHILE -> Mantém o sistema rodando em loop até o usuário escolher sair
while True:

    # EXIBIÇÃO -> Mostra o menu principal do sistema
    print("Sistema de Estoque de Produtos=")

    print("1 - Cadastrar Livros")
    print("2 - Listar Livros")
    print("3 - Atualizar Livro")
    print("4 - Remover Livro")
    print("5 - Valor total do Estoque")
    print("6 - Sair")

    # VARIÁVEL -> Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # IF -> Verifica se o usuário escolheu a opção 1
    if opcao == "1":

        # VARIÁVEL -> Guarda o nome do produto digitado pelo usuário
        nome = input("Nome do produto: ")

        # FOR -> Percorre a tupla de categorias e mostra as opções disponíveis
        for i in range(len(categorias)):
            print(i + 1, "-", categorias[i])

        # CONVERSÃO DE DADOS -> Converte a escolha da categoria para número inteiro
        escolha = int(input("Escolha a categoria: "))

        # CONVERSÃO DE DADOS -> Converte o preço para número decimal (float)
        preco = float(input("Preço: "))

        # CONVERSÃO DE DADOS -> Converte a quantidade para número inteiro
        quantidade = int(input("Quantidade: "))

        # DICIONÁRIO -> Cria um produto com todas as informações cadastradas
        produto = {
            "nome": nome,
            "categoria": categorias[escolha - 1],  # pega a categoria escolhida
            "preco": preco,
            "quantidade": quantidade
        }

        # LISTA -> Adiciona o produto criado dentro do estoque
        estoque.append(produto)

    # IF -> Verifica se o usuário escolheu a opção 2
    elif opcao == "2":

        # CONDIÇÃO -> Verifica se a lista está vazia
        if len(estoque) == 0:
            print("Nenhum produto cadastrado, por favor cadastre")

        else:

            # FOR -> Percorre todos os produtos dentro da lista estoque
            for produto in estoque:

                # EXIBIÇÃO -> Mostra os dados do produto
                print(livro["nome"])
                print(livro["categoria"])
                print(livro["preco"])
                print(livro["quantidade"])

                # IF -> Verifica se há estoque disponível
                if livro["quantidade"] > 0:
                    print("Disponível")
                else:
                    print("Sem estoque, precisa comprar")

    # IF -> Verifica se o usuário escolheu a opção 3
    elif opcao == "3":

        # VARIÁVEL -> Guarda o nome do produto que será buscado
        nome_busca = input("Nome do livro: ")

        # VARIÁVEL -> Controle para saber se encontrou o produto
        encontrado = False

        # FOR -> Percorre todos os produtos do estoque
        for produto in estoque:

            # IF -> Compara nomes ignorando maiúsculas e minúsculas
            if livro["nome"].lower() == nome_busca.lower():

                # VARIÁVEL -> Recebe nova quantidade informada pelo usuário
                nova_quantidade = int(input("Nova quantidade: "))

                # ATUALIZAÇÃO -> Atualiza a quantidade do produto
                livro["quantidade"] = nova_quantidade

                # MARCAÇÃO -> Indica que o produto foi encontrado
                encontrado = True

        # IF -> Caso nenhum produto tenha sido encontrado
        if encontrado == False:
            print("Livro não foi encontrado")

    # IF -> Verifica se o usuário escolheu a opção 4
    elif opcao == "4":

        # VARIÁVEL -> Guarda o nome do produto que será removido
        nome_busca = input("Nome do livro: ")

        # VARIÁVEL -> Controle de busca
        encontrado = False

        # FOR -> Percorre o estoque
        for produto in estoque:

            # IF -> Verifica se encontrou o produto
            if livro["nome"].lower() == nome_busca.lower():

                # REMOVE -> Remove o produto da lista
                estoque.remove(livro)

                # MARCAÇÃO -> Produto foi encontrado
                encontrado = True

                print("Livro removido com sucesso")

        # IF -> Caso não tenha encontrado o produto
        if encontrado == False:
            print("Livro não foi encontrado")

    # IF -> Verifica se o usuário escolheu a opção 5
    elif opcao == "5":

        # VARIÁVEL -> Armazena o valor total do estoque
        total = 0

        # FOR -> Percorre todos os produtos
        for produto in estoque:

            # CÁLCULO -> Soma preço x quantidade de cada produto
            total += livro["preco"] * livro["quantidade"]

        # EXIBIÇÃO -> Mostra o valor total do estoque
        print(f"Valor total das suas mercadorias {total:.2f}")

    # IF -> Verifica se o usuário escolheu a opção 6
    elif opcao == "6":
        # BREAK -> Encerra o sistema
        break

    # ELSE -> Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida.")

def obter_dados_livro():
    while True:
        titulo = input("Digite o título do livro: ").strip()
        if titulo:
            break
        print("Erro: O TÍTULO não pode estar vazio.")

    while True:
        autor = input("Digite o nome do autor: ").strip()
        if autor:
            break
        print("Erro: O AUTOR não pode estar vazio.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade > 0:
                break
            print("Erro: A quantidade deve ser MAIOR que ZERO.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    return titulo, autor, quantidade

def confirmar_remocao():
    while True:
        resposta = input("Deseja realmente remover? (S/N): ").strip().upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            print("Remoção cancelada.")
            return False
        else:
            print("Opção inválida. Digite apenas 'S' para Sim ou 'N' para Não.")

# Exemplo de uso na hora de excluir:
# if confirmar_remocao():
#     deletar_registro() # Substitua pela sua função de delete
