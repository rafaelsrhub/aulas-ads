def rejuste_salarial(salario,porcentagem):
    novo_salario=salario+(salario*porcentagem/100)
    return novo_salario

print('Qual o nome do funcionário?')
nome:str(input('Nome:'))
print('Qual o sálario atual do funcionário {nome}')
