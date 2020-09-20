from random import *

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

#deixe  o jogador fazer 3 tentativas
for attempt in range(3):
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
    print("Parabéns!")
  else:
    print("Que Peninha!")