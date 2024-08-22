login = 'admin'
senha = '123'
logininput = input('Digite o login:')
senhainput = input('Digite a senha:')
if logininput == login and senhainput == senha:
    print('Olá, seja bem-vindo!')
else:
    print('Login ou senha inválidos, tente novamente.')
