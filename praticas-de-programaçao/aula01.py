def calcular_media (n1,n2,n3):
    media = (n1+n2+n3)/3
    return media

def verificar_aprovação (media):
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


#web