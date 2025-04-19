#media aprovado maior ou igual a SETE

#cursa TRES materias
nota_port = float(input('Digite sua nota: '))
nota_mat = float(input('Digite sua nota: '))
nota_ing = float(input('Digite sua nota: '))

#o aluno precisa passar em TODAS as materias
#condicao SE aprovado
if (nota_port >= 7 and nota_mat >= 7 and nota_ing >= 7):
    print('Parabéns! Você foi aprovado!')
else:
    print('Reprovado, nos vemos na RECUPERAÇÃO!')