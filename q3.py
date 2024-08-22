nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
if idade >= 16:
  print(f'Olá {nome}, você está apta a votar.')
else:
  print(f'Olá {nome}, você não está apta a votar.')