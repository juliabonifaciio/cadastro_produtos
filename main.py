import os
from colorama import Fore, init

init(autoreset=True)

lista_dicionarios = [
    {
        "nome_produto": "Camisa de borracha feminina",
        "cod_produto": "001",
        "tipo": "vestuario",
        "quantidade_estoque": "10",
        "preco": "1299",
        "detalhes": "Roupa de borracha da marca ripcurl tamanho M",
        "fornecedor": "RipCurl"
    }
]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_subtitulo(texto):
    limpar_tela()
    print(Fore.CYAN + f"\n=== {texto.upper()} ===\n")

def voltar_ao_menu_principal():
    from main import voltar_ao_menu_principal as voltar
    voltar()

def finalizar_app():
    print(Fore.MAGENTA + "\n👋 Finalizando o sistema... Até logo!\n")

def estoque_adicionar_produto():
    exibir_subtitulo("Cadastro de Produtos")

    nome = input("Nome do produto: ").strip()
    if not nome:
        print(Fore.RED + "Nome não pode ser vazio!")
        return voltar_ao_menu_principal()

    categoria = input("Categoria (vestuario / calcado / acessorio): ").lower()

    if categoria not in ["vestuario", "calcado", "acessorio"]:
        print(Fore.RED + "Categoria inválida!")
        return voltar_ao_menu_principal()

    novo_produto = {
        "nome_produto": nome,
        "cod_produto": str(len(lista_dicionarios) + 1).zfill(3),
        "tipo": categoria,
        "quantidade_estoque": "0",
        "preco": "0"
    }

    lista_dicionarios.append(novo_produto)

    print(Fore.GREEN + f"\n✅ Produto '{nome}' cadastrado com sucesso!")

    voltar_ao_menu_principal()

def estoque_excluir_produto():
    exibir_subtitulo("Excluir Produto")

    nome = input("Nome do produto: ")

    for produto in lista_dicionarios:
        if produto["nome_produto"].lower() == nome.lower():
            lista_dicionarios.remove(produto)
            print(Fore.GREEN + "Produto removido com sucesso!")
            return voltar_ao_menu_principal()

    print(Fore.RED + "Produto não encontrado!")
    voltar_ao_menu_principal()

def listar_produtos():
    exibir_subtitulo("Produtos em Estoque")

    if not lista_dicionarios:
        print(Fore.YELLOW + "Nenhum produto cadastrado.")
        return voltar_ao_menu_principal()

    for produto in lista_dicionarios:
        print(Fore.BLUE + "-" * 40)
        print(Fore.WHITE + f"📦 {produto['nome_produto']}")
        print(f"Código: {produto['cod_produto']}")
        print(f"Tipo: {produto['tipo']}")
        print(f"Estoque: {produto['quantidade_estoque']}")
        print(f"Preço: R$ {produto['preco']}")

    voltar_ao_menu_principal()

def estoque_atualizar():
    exibir_subtitulo("Atualizar Estoque")

    nome = input("Produto: ")

    for produto in lista_dicionarios:
        if produto["nome_produto"].lower() == nome.lower():
            nova_qtd = input("Nova quantidade: ")
            produto["quantidade_estoque"] = nova_qtd
            print(Fore.GREEN + "Estoque atualizado!")
            return voltar_ao_menu_principal()

    print(Fore.RED + "Produto não encontrado!")
    voltar_ao_menu_principal()

def estoque_alerta():
    exibir_subtitulo("Alerta de Estoque (< 50)")

    encontrou = False

    for produto in lista_dicionarios:
        if int(produto["quantidade_estoque"]) < 50:
            print(Fore.RED + f"{produto['nome_produto']} - {produto['quantidade_estoque']}")
            encontrou = True

    if not encontrou:
        print(Fore.GREEN + "Nenhum produto com estoque baixo!")

    voltar_ao_menu_principal()
