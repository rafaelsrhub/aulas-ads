# ============================================
# SISTEMA DE CONTROLE DE ESTOQUE
# Disciplina: Práticas de Programação
# ============================================
estoque = [] # lista de dicionários com os produtos
def cadastrar_produto(estoque):
  print("\n--- CADASTRAR PRODUTO ---")
  codigo = int(input("Digite o código do produto: "))
  for produto in estoque:
    if produto["codigo"] == codigo:
      print("Erro: já existe um produto com esse código!")
      return
  nome = input("Digite o nome do produto: ")
  preco = float(input("Digite o preço do produto: R$ "))
  if preco < 0:
    print("Erro: o preço não pode ser negativo!")
    return
  quantidade = int(input("Digite a quantidade em estoque: "))
  if quantidade < 0:
    print("Erro: a quantidade não pode ser negativa!")
    return
  novo_produto = {
    "codigo": codigo,
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
  }
  estoque.append(novo_produto)
  print(f"Produto '{nome}' cadastrado com sucesso!")
def calcular_total(estoque):
  print("\n--- TOTAL DE PRODUTOS EM ESTOQUE ---")
  if len(estoque) == 0:
    print("Nenhum produto cadastrado.")
    return
  total = 0
  for produto in estoque:
    total = total + produto["quantidade"]
  print(f"Total de produtos em estoque: {total} unidades")
def menu():
  while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar Produto")
    print("2 - Calcular Total de Produtos em Estoque")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
      cadastrar_produto(estoque)
    elif opcao == "2":
      calcular_total(estoque)
    elif opcao == "0":
      print("Encerrando o sistema. Até logo!")
      break
    else:
      print("Opção inválida! Tente novamente.")
# Inicia o programa
menu()