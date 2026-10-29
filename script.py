python
def calcular_juros_compostos(capital_inicial, taxa_mensal, meses, meta_financeira):
    """
    Calcula a evolução de um capital sob juros compostos mês a mês
    e valida se o objetivo financeiro foi atingido.
    """
    # Validação de segurança dos dados de entrada
    if capital_inicial <= 0 or taxa_mensal < 0 or meses <= 0:
        return {
            "status": "erro",
            "mensagem": "Os valores de entrada devem ser positivos e maiores que zero."
        }
    
    historico_saldos = []
    saldo_atual = capital_inicial
    
    # Processamento iterativo mês a mês
    for mes in range(1, meses + 1):
        saldo_atual = saldo_atual * (1 + taxa_mensal)
        historico_saldos.append(round(saldo_atual, 2))
    
    # --- REGRA DE NEGÓCIO ---
    # Verifica se o montante final atingiu ou superou a meta estabelecida
    meta_atingida = saldo_atual >= meta_financeira
    
    return {
        "status": "sucesso",
        "montante_final": round(saldo_atual, 2),
        "historico": historico_saldos,
        "meta_atingida": meta_atingida,
        "mensagem_negocio": "Objetivo Concluído: Meta financeira ALCANÇADA!" if meta_atingida else "Objetivo Pendente: Meta financeira NÃO ALCANÇADA."
    }

# ==============================================================================
# BLOCO PRINCIPAL: CASOS DE TESTE PARA EXECUÇÃO
# ==============================================================================
if __name__ == "__main__":
    print("=== INICIANDO SIMULAÇÕES FINANCEIRAS ===\n")
    
    # --- TESTE 1: Cenário com Meta Alcançada ---
    print("--- Executando Teste 1 (Meta Viável) ---")
    resultado_1 = calcular_juros_compostos(
        capital_inicial=1000.00, 
        taxa_mensal=0.02, 
        meses=12, 
        meta_financeira=1200.00
    )
    
    if resultado_1["status"] == "sucesso":
        print(f"Investimento Inicial: R$ 1000.00")
        print(f"Montante Final Acumulado: R$ {resultado_1['montante_final']}")
        print(f"Evolução dos 3 primeiros meses: {resultado_1['historico'][:3]}...")
        print(f"Resultado da Regra de Negócio: {resultado_1['mensagem_negocio']}\n")

    # --- TESTE 2: Cenário com Meta Não Alcançada ---
    print("--- Executando Teste 2 (Meta Muito Alta para o Prazo) ---")
    resultado_2 = calcular_juros_compostos(
        capital_inicial=500.00, 
        taxa_mensal=0.01, 
        meses=6, 
        meta_financeira=600.00
    )
    
    if resultado_2["status"] == "sucesso":
        print(f"Investimento Inicial: R$ 500.00")
        print(f"Montante Final Acumulado: R$ {resultado_2['montante_final']}")
        print(f"Histórico Completo Mês a Mês: {resultado_2['historico']}")
        print(f"Resultado da Regra de Negócio: {resultado_2['mensagem_negocio']}\n")

    print("=== FIM DA EXECUÇÃO ===")
