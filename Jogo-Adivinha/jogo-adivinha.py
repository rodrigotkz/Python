secreto = 'perfume'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break


    letra = input('Digite uma letra: ')

    if len(letra) > 1:
       print('A isso não vale!!, digite apenas uma letra.')
       continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUL!, a letra "{letra}" existe na palavra.')
    else:
        print(f'F, a letra "{letra}" Não existe na palavra.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal!, você GANHOU! GGWP, A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

        print(f'Você ainda tem {chances} chances.')
        print()