import copy

#função para dar realce ao programa
def realce():
    print("-" * 55)

#função para gerar o ID
id_global = 0

def gerar_id():
    global id_global
    id_global += 1
    return id_global

#função para cadastro dos livros
def cadastrar_livro():
    print('-' * 15, 'MENU CADASTRAR LIVRO', '-' * 24)
    print(f'Id do livro: {gerar_id()}') #mostra o id que foi gerado
    global nome_livro, auto_livro, editora
    nome_livro = input('Entre com o nome do livro: ') #pede para o usuario digitar o nome do livro
    auto_livro = input('Entre com o autor do livro: ') #pede para o usuario digitar o autor do livro
    editora = input('Entre com a editora do livro: ') #pede pro usuario digitar a editora do livro

# funcao para consulta de livro com if e elif para verificar qual numero usuario digitou
def consultar_livro():
    print('-' * 15, 'MENU CONSULTAR LIVRO(S)', '-' * 24)
    print('Escolha a opção desejada: \n'
          '1. Consultar todos\n'
          '2. Consultar por ID\n'
          '3. Consultar por autor\n'
          '4. Retornar ao menu')
    consulta = input('>> ')
    if consulta == '1':
        listar_livros(lista_livro) # consulta todos o livros
    elif consulta == '2':
        id_busca = int(input("Digite o ID do livro: ")) # consulta os livros por ID
        realce()
        for livro in lista_livro:
            if livro['ID'] == id_busca:
                listar_livros([livro])
                break
        else:
            print("Livro com esse ID não encontrado.")
    elif consulta == '3':
        autor_busca = input("Digite o nome do autor: ").lower() #consulta os livros por autor
        encontrados = [livro for livro in lista_livro if livro['Autor'].lower() == autor_busca]

        if encontrados:
            for livro in encontrados: #exibe os livros que foram encontrados
                listar_livros(encontrados)
        else:
            print("Nenhum livro encontrado para esse autor.")

# função para listar os livros
def listar_livros(lista):
    if not lista: # faz a verificação se a lista está vazia
        print("Nenhum livro encontrado.")
        return

    for livro in lista: #exibe cada livro da lista
        print(f"ID: {livro['ID']}")
        print(f"Nome: {livro['Nome']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Editora: {livro['Editora']}")
        print("-" * 40)
        realce()

#função para remover livro com base no ID digitado
def remover_livro():
    print('-' * 15, 'REMOVER LIVRO', '-' * 24)
    try:
        id_remover = int(input("Digite o ID do livro que deseja remover: ")) #solicita o id do livro a ser removido
        for i, livro in enumerate(lista_livro): #varre a lista de livros com o indice
            if livro['ID'] == id_remover: # verifica se o id corresponde ao que foi digitado
                del lista_livro[i] # remove o livro da lista
                print("Livro removido com sucesso.")
                return
        print("Livro com esse ID não encontrado.")
    except ValueError: # tratação de erro caso o usuario digite um valor invalido
        print("ID inválido.")

#programa principal

lista_livro = [] # lista para armazenar os livros
dicionario_de_livros = {} # cria um dicionario para armazenar as informações do livro


print('Bem-Vindo a livraria do Kaua de Souza')
while True:
    try:
        print('-'*55)
        print('-'*15, 'MENU PRINCIPAL', '-'*24)

        #mostra as opções do menu principal
        escolha = int(input('Escolha a opção desejada: \n'
              '1 - Cadastrar Livro\n'
              '2 - Consultar Livro(s)\n'
              '3 - Remover Livro\n'
              '4 - Sair\n'))
    except ValueError: #trata o erro caso o usuario digite um valor invalido
        print("Opção inválida.")

#bloco de codigo para verificar as escolhas do usuario
    if escolha == 1:
        realce()
        cadastrar_livro() # chama a função para cadastro do livro
        # variavel da lista e dicionario
        realce()
        # adicionando as informações do livro ao dicionario
        dicionario_de_livros['Nome'] = nome_livro #atribui o nome inserido ao livro
        dicionario_de_livros['Autor'] = auto_livro #atribui o auto inserido ao livro
        dicionario_de_livros['Editora'] = editora #atribui a editora inserida ao livro
        dicionario_de_livros['ID'] = id_global # atribui o id gerado ao livro
        lista_livro.append(dicionario_de_livros.copy()) # copiando o conteudo do dicionario para uma lista
    elif escolha == 2:
        realce()
        consultar_livro() # chama a função para consultar o livro

    elif escolha == 3:
        remover_livro() # chama a função para remover o livro

    elif escolha == 4:
        print('Saindo do Programa...') # encerra o programa
        break
    else:
        print("Opção inválida tente novamente.")


