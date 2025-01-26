for i in range(1, 10):
    if i == 2:
        print("Vou pular a linha 2")
        continue

    # if i == 8:
    #     print("Vou parar na linha 8")
    #     break

    for j in range(1, 3):
        print(i, j)
else:
    print("O laço foi concluído")