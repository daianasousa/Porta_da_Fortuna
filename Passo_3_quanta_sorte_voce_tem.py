from random import *

#essa variável guarda o número de vezes que o jogo já foi jogado
tentativas = 0


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

#repita enquanto a variável score for menor do que 3 
while score < 3:


  #soma 1 ao número de tentativas
  tentativas = tentativas + 1
  print("\nTentativa", tentativas, ": Escolha uma porta (1, 2 or 3):")
 
  #pegue a porta escolhida e a armazene como um número inteiro (int)
  portaescolhida = input()
  portaescolhida = int(portaescolhida)

  #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
  portacerta = randint(1, 3)

  #mostre ao jogador qual porta ele escolheu e qual era a porta certa
  print("A porta escolhida foi a", portaescolhida)
  print("A porta Certa é a", portacerta)
  
  #O jogador ganha se o número da porta escolhida e o número da porta certa forem o mesmo
  if portaescolhida == portacerta:
    score += 1
    print("Parabéns!")
  else:
    print("Que Peninha!")
  
  print("Sua portuação atual é", score)

print("\n** Você conseguiu! Terminou o jogo em", tentativas, "tentativas **")