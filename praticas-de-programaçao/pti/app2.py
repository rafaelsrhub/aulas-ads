# nesta versão usei a ia para gerar alguns codigos que eu gostaria de incrementar como função
#importei a biblioteca random para gerar o id do produto
import random

# aqui o banco de dados onde será armazenado 
estoque = []

#Função que gera um id randomizado e automatizado para cada item cadastrado
def gerar_id():
    while True:
        #como o numero id funciona como uma chave e não como numero para calculo
        #usei str(para definir como um texto) e zfill (para que o numero tenha sempre 5 digitos)
        novo_id = str(random.randint(1, 99999)).zfill(5)
        if not any(p['id_produto'] == novo_id for p in estoque):
            return novo_id

#função que inicia a busca de um produto no estoque pelo id
def buscar(id):
    # Trata o código para garantir que tenha 5 dígitos (ex: '5' vira '00005')
    cinco_digitos_id = id.zfill(5)
    for p in estoque:
        if p['id_produto'] == cinco_digitos_id:
            return p
    return None

#criei uma função para tratar o valor fornecido pelo usuario na entrada dos preços
#agora o usuario pode utilizar o valor tanto com "." quanto com ","
def tratar_valor(valor_str):
    return float(valor_str.replace(',', '.'))

#esse é o menu de gestão dos produtos
def menu_gestao():
    while True:
        print("\n--- [1] GESTÃO DE PRODUTOS ---")
        print("Escolha uma nova opção")
        print("1. Cadastrar Novo")
        print("2. Excluir Produto")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            id_p = gerar_id()
            print(f"\nID Gerado: {id_p}")
            nome = input("Nome do produto: ")
            try:
                p_compra = tratar_valor(input("Preço Compra (R$): "))
                p_venda = tratar_valor(input("Preço Venda (R$): "))
                qtd = int(input("Quantidade inicial: "))
                
                lucro = p_venda - p_compra
                
                estoque.append({
                    "codigo": id_p, 
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
            id_busca = input("ID para excluir: ")
            p = buscar(id_busca)
            if p:
                estoque.remove(p)
                print(f"Produto {p['nome']} removido.")
            else:
                print("ID não encontrado.")
        elif opcao == '0':
            break

# --- 2. COMPRA E VENDA (Lógica corrigida para não sair do loop) ---

def menu_movimentacao():
    while True:
        print("\n--- [2] COMPRA E VENDA ---")
        print("1. Registrar Compra (Aumentar Qtd)")
        print("2. Registrar Venda (Diminuir Qtd)")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao in ['1', '2']:
            id_busca = input("Digite o ID do produto: ")
            p = buscar(id_busca)
            
            if not p:
                print("Erro: Produto não encontrado!")
                continue

            try:
                qtd_mov = int(input(f"Quantidade para {'Aumentar' if opcao == '1' else 'Vender'}: "))
                if qtd_mov <= 0:
                    print("Erro: A quantidade deve ser maior que zero.")
                    continue

                if opcao == '1': # COMPRA
                    p['quantidade'] += qtd_mov
                    print(f"Sucesso! {p['nome']} agora tem {p['quantidade']} unidades.")
                
                elif opcao == '2': # VENDA
                    if qtd_mov <= p['quantidade']:
                        p['quantidade'] -= qtd_mov
                        faturamento = qtd_mov * p['p_venda']
                        print(f"Venda Realizada! Total: R$ {faturamento:.2f}")
                        print(f"Estoque atual de {p['nome']}: {p['quantidade']}")
                    else:
                        print(f"Erro: Estoque insuficiente! (Disponível: {p['quantidade']})")
            except ValueError:
                print("Erro: Digite um número inteiro para a quantidade.")
        
        elif opcao == '0':
            break

# --- 3. RELATÓRIO (MOSTRANDO EM REAIS R$) ---

def exibir_relatorio():
    print("\n" + "="*85)
    print(f"{'ID':<7} | {'NOME':<15} | {'COMPRA':<12} | {'VENDA':<12} | {'LUCRO':<10} | {'QTD':<5}")
    print("-" * 85)
    
    if not estoque:
        print("Estoque vazio.")
    else:
        for p in estoque:
            
            print(f"{p['codigo']:<7} | "
                  f"{p['nome']:<15} | "
                  f"R$ {p['p_compra']:>8.2f} | "
                  f"R$ {p['p_venda']:>8.2f} | "
                  f"R$ {p['lucro']:>8.2f} | "
                  f"{p['quantidade']:<5}")
    print("="*85)

def menu_principal():
    #loop que gerencia menu principal
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

if __name__ == "__main__":
    menu_principal()