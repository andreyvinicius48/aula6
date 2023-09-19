for i in range(10):
    if i == 2:
        print('1 e 2, pulamdo...')
        continue

    if i == 8:
        print('1 e 8, seu else nao excutara')
        break

    for j in range(1, 3):
        print(i, j)
    else:
        print('for completo com sucesso')
