import random

estoque = []

def gerar_id():
    while True:
        novo_id = str(random.randint(1, 99999)).zfill(5)
        if not any(p['id_produto'] == novo_id for p in estoque):
            return novo_id

def buscar(id_produto_busca):
    id_formatado = id_produto_busca.zfill(5)
    for p in estoque:
        if p['id_produto'] == id_formatado:
            return p
    return None

def tratar_valor(valor_str):
    return float(valor_str.replace(',', '.'))

def menu_gestao():
    while True:
        print("\n--- GESTÃO DE PRODUTOS ---")
        print("1. Cadastrar Novo")
        print("2. Excluir Produto")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            id_prod = gerar_id()
            print(f"\nID Gerado: {id_prod}")
            nome = input("Nome do produto: ")
            try:
                p_compra = tratar_valor(input("Preço Compra (R$): "))
                p_venda = tratar_valor(input("Preço Venda (R$): "))
                qtd = int(input("Quantidade inicial: "))
                lucro = p_venda - p_compra
                
                estoque.append({
                    "id_produto": id_prod, 
                    "nome": nome, 
                    "p_compra": p_compra, 
                    "p_venda": p_venda, 
                    "lucro": lucro, 
                    "quantidade": qtd
                })
                print(f"Produto '{nome}' cadastrado com sucesso!")
            except ValueError:
                print("Erro! Use apenas números e vírgula/ponto para preços.")

        elif opcao == '2':
            id_para_excluir = input("ID do produto para excluir: ")
            p = buscar(id_para_excluir)
            if p:
                estoque.remove(p)
                print(f"Produto {p['nome']} removido.")
            else:
                print("ID não encontrado.")
        elif opcao == '0':
            break

def menu_movimentacao():
    while True:
        print("\n--- [2] COMPRA E VENDA ---")
        print("1. Registrar Compra ")
        print("2. Registrar Venda ")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao in ['1', '2']:
            id_busca = input("Digite o ID do produto: ")
            p = buscar(id_busca)
            
            if not p:
                print("Erro: Produto não encontrado!")
                continue

            try:
                qtd_mov = int(input(f"Quantidade {'Vendida' if opcao == '1' else 'Vender'}: "))
                if qtd_mov <= 0:
                    print("Erro: A quantidade deve ser maior que zero.")
                    continue

                if opcao == '1':
                    p['quantidade'] += qtd_mov
                    print(f"Sucesso! {p['nome']} agora tem {p['quantidade']} unidades.")
                
                elif opcao == '2':
                    if qtd_mov <= p['quantidade']:
                        p['quantidade'] -= qtd_mov
                        faturamento = qtd_mov * p['p_venda']
                        print(f"Venda Realizada! Total: R$ {faturamento:.2f}")
                        print(f"Estoque atual de {p['nome']}: {p['quantidade']}")
                    else:
                        print(f"Erro: Estoque insuficiente!")
            except ValueError:
                print("Erro: Digite um número inteiro.")
        
        elif opcao == '0':
            break

def exibir_relatorio():
    print("\n" + "="*85)
    print(f"{'ID PROD':<10} | {'NOME':<15} | {'COMPRA':<12} | {'VENDA':<12} | {'LUCRO':<10} | {'QTD':<5}")
    print("-" * 85)
    
    if not estoque:
        print("Estoque vazio.")
    else:
        total_produtos_estoque = 0
        for p in estoque:
            total_produtos_estoque += p['quantidade']
            print(f"{p['id_produto']:<10} | "
                  f"{p['nome']:<15} | "
                  f"R$ {p['p_compra']:>8.2f} | "
                  f"R$ {p['p_venda']:>8.2f} | "
                  f"R$ {p['lucro']:>8.2f} | "
                  f"{p['quantidade']:<5}")
        
        print("-" * 85)
        print(f"{'TOTAL DE PRODUTOS NO ESTOQUE:':<78} {total_produtos_estoque}")
    
    print("="*85)

def menu_principal():
    while True:
        print("\n========== CONTROLE DE ESTOQUE ==========")
        print("1. Gestão (Cadastrar/Excluir)")
        print("2. Movimentação (Compra/Venda)")
        print("3. Inventário")
        print("0. Sair")
        
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            menu_gestao()
        elif opcao == '2':
            menu_movimentacao() 
        elif opcao == '3':
            exibir_relatorio()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção Inválida!")
    
menu_principal()