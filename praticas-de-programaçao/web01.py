def mostra (nome):
    print(f"Olá {nome}, bem vindo ao meu novo mundo")

nome=input('Qual o seu nome?')
mostra(nome)

def filme_em_cartaz(filme):
    filmes=['panico','alagado','piratas','gentegrande']
    if filme in filmes:
        return 'Em cartaz'
    else:
        return 'Filme não está em cartaz'
    
print('Qual o nome do filme que você gostaria de assistir?')
filme=str(input('Filme:'))
cartaz=filme_em_cartaz(filme)
print(cartaz)
