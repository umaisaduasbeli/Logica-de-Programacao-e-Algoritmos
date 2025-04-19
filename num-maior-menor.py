# programa recebe dois valores
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

# condição SE o valor num1 é maior que o num2
if (num1 > num2):
    # printar na tela informando que é maior, essa etapa transforma em uma condição composta.
    print(f'O número {num1} é maior que o número {num2}.')
else:
    print(f'O numero {num2} é maior que {num1}')