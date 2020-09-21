from random import *

#o usuário usa está variável para continuar jogando
jogando = True

pontuacao = 0


#O jogador vai tenta fazer  exatamentes 21 pontos
print('''
Vinte e um!
===========
Tente Fazer 21 pontos!
''')

#repetir, enquanto a variavel 'jogando' estiver com o valor 'True' (Verdadeiro)
while jogando == True:

  #Vai gerar um número aleatório (entre 1 e 10)
  aleatorio = randint(1, 10)

  #Vai soma a minha pontuação com o número gerado
  pontuacao += aleatorio

  #Vai mostrar o proxímo número que foi gerado
  print(f'Seu proxímo número é {aleatorio}')
  
  #Vai mostra a minha pontuação atual
  print(f'Sua pontuação agora é {pontuacao}')
  
  
  #Pergunte ao jogador se ele quer continuar jogando
  print("\nGostaria de somar mais um número? (s/n)")
  resposta = input().lower()

  #Se o jogador digitar 'n', continuará com a pontuação atual 
  if resposta == 'n' or resposta == 'nao':
    jogando = False

  
print(f'Sua pontuação final é {pontuacao}')

if pontuacao == 21:
  print("Parabéns, você VENCEU!")
else:
  print("Que pena, você PERDEU!")