print('Bem vindo a calculadora!')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resultado = 0
opr = input('Qual operação deseja realizar? (multiplicacao, soma, subtracao ou divisao) '.lower())
if opr == 'multiplicacao':
    resultado = n1 * n2
    print(resultado)
elif opr == 'soma':
    resultado = n1 + n2
    print(resultado)
elif opr == 'subtracao':
    resultado = n1 - n2
    print(resultado)
elif opr == 'divisao':
    resultado = n1 / n2
    print(resultado)


