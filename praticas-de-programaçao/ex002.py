pecas=[48.5,49.3,49.7,50,49.5]

def separar_pecas_pt(mm_min,mm_max):
    pecas_intervalo=[]
    for p in pecas:
        if p >= mm_min and p <= mm_max:
            pecas_intervalo.append(p)
    return pecas_intervalo
def verificar_entrada(entrada):
    try:
        return float(entrada.replace(',','.')
                     )
    except ValueError:
        return 'quit'

def pesquisa_peça():
    while True:
        print(f'{('*=*'*25)}')
        print('A seguir insira o intervalo em milimetros que você precisa de peça')
        print('Ou insira qualquer letra para sair!')
        print(f'{('*=*'*25)}')
        mm_min=verificar_entrada(input('Milimetros Minimos:'))
        if mm_min=='quit':
            break
        mm_max=verificar_entrada(input('Milimetros Maximo: '))
        if mm_max== 'quit':
            break

        pecas_intervalo=separar_pecas_pt(mm_min,mm_max)
        if len(pecas_intervalo)==0:
            print('Nenhuma peça encontrada entre essas milimetragens')
        else:           
            for i in pecas_intervalo:
                print(f'Peça de: {i}mm Disponível')

pesquisa_peça()