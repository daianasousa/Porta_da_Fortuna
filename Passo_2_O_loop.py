from random import *

#o usuário muda esta variável para terminar o jogo 

jogando = True

score = 0

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=========


Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual e a porta certa para ganhar o prêmio!

 ______   ______   ______
|      | |      | |      |
|  [1] | |  [2] | | [3]  |
|    o | |    o | |   o  | 
|______| |______| |______| 
''')

#repetir, enquanto a variavel 'jogando' estiver com o valor 'True' (Verdadeiro)
while jogando == True:
  print("\nEscolha uma porta (1, 2, 3):")
  
  #pegue a porta escolhida e a armazene como um número inteiro (int)
  portaescolhida = input()
  portaescolhida = int(portaescolhida)

  #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e  3)
  portacerta = randint(1,3)

  #mostre ao jogador qual porta ele escolheu e qual era a porta certa
  print("A porta escolhida foi a", portaescolhida)
  print("A porta Certa é a", portacerta)
  
  #O jogador ganha se o número da porta escolhida e o número da porta certa forem o mesmo
  if portaescolhida == portacerta:
    score += 1
    print("Parabéns!")
  else:
    print("Que Peninha!")
  
  print("Sua portuação é", score)

  #Pergunte ao jogador se ele quer continuar jogando
  print("\nVocê quer jogar de novo? (s/n)")
  resposta = input()
  #Termina o jogo se o jogador digitar 'n'
  if resposta == 'n':
    jogando = False

print('Obrigado por jogar.')
print("Sua pontuação final é de", score)