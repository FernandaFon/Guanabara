import random
jkp=int(input('Vamos jogar JoKenPo!\nSuas opções são:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\nQual sua jogada? '))
ran=random.choice([1,2,3])
if jkp == 1:
    print('Você escolheu pedra')
    if jkp == ran:
        print('Eu também escolhi pedra\nEMPATE')
    elif ran == 2:
        print('Eu escolhi papel\nEu ganhei haha!')
    else:
        print('Eu escolhi tesoura\nParabéns! Você ganhou.')
elif jkp == 2:
    print('Você escolheu papel')
    if ran == 2:
        print('Eu escolhi papel também\nEMPATE')
    elif ran == 1:
        print('Eu escolhi pedra\n Parabéns, você ganhou!')
    else:
        print('Eu escolhi tesoura\nEu ganhei haha!')
elif jkp == 3:
    print('Você escolheu tesoura')
    if ran == 1:
        print('Eu escolhi pedra\nEu ganhei haha.')
    elif ran == 2:
        print('Eu escolhi papel.\nParabéns, você ganhou!')
    else:
        print('Eu também escolhi tesoura\nEmpate.')
else:
    print('Valor inválido, tente novamente.')
