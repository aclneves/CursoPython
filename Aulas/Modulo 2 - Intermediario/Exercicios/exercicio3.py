# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
total_acertos = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta['Pergunta'])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")

    print()
    resposta = input("Escolha uma opção: ")

    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta["Resposta"]:
                acertou = True
                total_acertos += 1

    if acertou:
        print("Acertou!!")
    else:
        print("Errou")
    print()

if total_acertos > 0:
    print("Parabéns, você acertou", total_acertos, "de", len(perguntas), "perguntas")
else:
    print("Você não acertou nenhuma pergunta")
