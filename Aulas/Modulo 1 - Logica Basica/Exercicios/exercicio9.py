"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de insrir, apagar e listar os valores
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

import os

lista_compras = []

while True:
    print("O que você deseja fazer na sua lista de compras?")
    operacao = input("[I]nserir item, [A]apagar item, [L]istar itens\n").lower()

    if operacao == "i":
        os.system("clear")
        item = input("Digite o nome do item que deseja inserir: ").strip()
        if item.isalpha():
            lista_compras.append(item)
        else:
            print("Digite um item válido.")

    elif operacao == "a":
        os.system("clear")
        item_para_apagar = input("Digite o índice do item a ser apagado: ")
        try:
            item_para_apagar = int(item_para_apagar)
            lista_compras.pop(item_para_apagar)
        except IndexError:
            print("Não existe este índice na lista")
        except ValueError:
            print("Favor digitar um número inteiro")
        except Exception:
            print("Erro desconhecido")

    elif operacao == "l":
        os.system("clear")
        if not lista_compras:
            print("A lista está vazia, favor inserir algum item.")
        else:
            for index, nome in enumerate(lista_compras):
                print(index, nome)

    else:
        print("Por favor escolha uma opção correta")
        print("I - Inserir, A - Apagar, L - Listar")
