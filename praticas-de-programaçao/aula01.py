def calcular_media (n1,n2,n3):
    #criando uma vafriavel local
    media = (n1+n2+n3)/3
    return media 
    #também podemos definir o return de uma outra forma
    # return (n1+n2+n3)/3
    #ou
    #soma=n1+n2+n3
    #return soma/3
    '''porem por preferencia decidi que a primeira versão é mais organizada e visualmente legível'''
def verificar_aprovação (media):
    #definimos o retorno da aprovação
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"
    
def exibir_resultado (nome,media,resutado):
    print(f"Aluno: {nome}")
    print(f'Média: {media:.2f}')
    print(f'Resultado: {resutado}')


nome=input('Qual o nome do aluno')
n1=float(input('Qual a primeira nota do aluno?'))
n2=float(input('Qual a segunda nota do aluno?'))
n3=float(input('Qual a terceira nota do aluno?'))

media= calcular_media(n1,n2,n3)
resultado= verificar_aprovação(media)
exibir_resultado(nome,media,resultado)

