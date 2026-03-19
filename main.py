import os
from colorama import Fore, Style, init
from funcoes import *

init(autoreset=True)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_nome_do_programa():
    print(Fore.CYAN + "=" * 50)
    print(Fore.MAGENTA + "   MAJ COMÉRCIO DE SPORTSWEAR")
    print(Fore.CYAN + "=" * 50)

def exibir_opcoes():
    print(Fore.YELLOW + "\n📋 MENU PRINCIPAL\n")
    print("1 - ➕ Adicionar produto")
    print("2 - ❌ Excluir produto")
    print("3 - 🔄 Atualizar estoque")
    print("4 - ⚠️  Alerta de estoque")
    print("5 - 📦 Listar produtos")
    print("0 - 🚪 Sair\n")

def voltar_ao_menu_principal():
    input(Fore.BLUE + "\nPressione ENTER para voltar ao menu...")
    main()

def opcao_invalida():
    print(Fore.RED + "❌ Opção inválida!")
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao = int(input(Fore.GREEN + "Escolha uma opção: "))

        if opcao == 1:
            estoque_adicionar_produto()
        elif opcao == 2:
            estoque_excluir_produto()
        elif opcao == 3:
            estoque_atualizar()
        elif opcao == 4:
            estoque_alerta()
        elif opcao == 5:
            listar_produtos()
        elif opcao == 0:
            finalizar_app()
            return False
        else:
            opcao_invalida()
            return True

    except ValueError:
        print(Fore.RED + "Digite um número válido!")
        voltar_ao_menu_principal()

def main():
    while True:
        limpar_tela()
        exibir_nome_do_programa()
        exibir_opcoes()
        if not escolher_opcoes():
            break

if __name__ == "__main__":
    main()
