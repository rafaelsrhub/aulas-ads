def reajuste_salarial(salario,porcentagem):
    reajuste=(salario*porcentagem/100)
    return reajuste+salario
print('Qual o salário atual do colaborador?')
salario=float(input('Salário atual: '))
print('Qual a porcentagem de aumento')
aumento=float(input('Aumento em porcentagem: '))

print(f'O novo salário do colaborador é de: {reajuste_salarial(salario,aumento)} R$')