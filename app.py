import os

restaurantes = [
    {"nome": "Bella Massa", "categoria": "Italiana", "ativo": True},
    {"nome": "Sushi House", "categoria": "Japonesa", "ativo": False},
    {"nome": "Churrasquim", "categoria": "Brasileira", "ativo": True}
]

def exibir_titulo():
    # Cores ANSI para o efeito
    COR1 = '\033[38;5;196m' # Vermelho
    COR2 = '\033[38;5;202m' # Laranja
    COR3 = '\033[38;5;208m' # Laranja-Amarelado
    COR4 = '\033[38;5;214m' # Amarelo-Laranja
    COR5 = '\033[38;5;220m' # Amarelo
    COR6 = '\033[93m'       # Amarelo-Claro
    NEGRITO = '\033[1m'
    RESET = '\033[0m'
    
    arte_ascii = r"""
███████╗ █████╗ ██████╗  ██████╗ ██████╗     ███████╗██╗  ██╗██████╗ ██████╗ ███████╗███████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
███████╗███████║██████╔╝██║   ██║██████╔╝    █████╗   ╚███╔╝ ██████╔╝██████╔╝█████╗  ███████╗███████╗
╚════██║██╔══██║██╔══██╗██║   ██║██╔══██╗    ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
███████║██║  ██║██████╔╝╚██████╔╝██║  ██║    ███████╗██╔╝ ██╗██║     ██║  ██║███████╗███████║███████║
╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
"""

    linhas = arte_ascii.strip('\n').split('\n')
    cores = [COR1, COR2, COR3, COR4, COR5, COR6]
    
    print() # Linha em branco para espaçamento
    for i, linha in enumerate(linhas):
        cor_da_linha = cores[i % len(cores)]
        print(cor_da_linha + NEGRITO + linha + RESET)
    
    print("\n" + " " * 25 + "Bem-vindo ao Sabor Express!" + "\n")

def exibir_menu():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar restaurante")
    print("4 - Sair da aplicação\n")

def cadastrar_restaurante():
    nome = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")
    novo_restaurante = {"nome": nome, "categoria": categoria, "ativo": False}
    restaurantes.append(novo_restaurante)
    print(f"Restaurante '{nome}' cadastrado com sucesso!\n")

def listar_restaurantes():
    if not restaurantes:
        print("Nenhum restaurante cadastrado.\n")
        return
    print("\nRestaurantes cadastrados:")
    for idx, r in enumerate(restaurantes, 1):
        status = "Ativo" if r["ativo"] else "Inativo"
        print(f"{idx}. {r['nome']}".ljust(25) + f" | Categoria: {r['categoria']}".ljust(25) + f" | Status: {status}")
    print()

def ativar_restaurante():
    listar_restaurantes()
    try:
        escolha = int(input("Digite o número do restaurante para ativar/desativar: "))
        if 1 <= escolha <= len(restaurantes):
            restaurante = restaurantes[escolha - 1]
            restaurante["ativo"] = not restaurante["ativo"]
            status = "ativado" if restaurante["ativo"] else "desativado"
            print(f"Restaurante '{restaurante['nome']}' {status}!\n")
        else:
            print("Opção inválida.\n")
    except ValueError:
        print("Entrada inválida. Digite um número.\n")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_titulo()
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_restaurante()
        elif opcao == "2":
            listar_restaurantes()
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            ativar_restaurante()
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            print("Saindo da aplicação. Até logo!")
            break
        else:
            print("Opção inválida.\n")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()