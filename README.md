markdown
# 📈 Simulador de Juros Compostos e Tomada de Decisão Financeira

Este projeto consiste em um motor de processamento em Python que simula a evolução de um capital ao longo do tempo sob a aplicação de juros compostos. O objetivo é apoiar desenvolvedores e estudantes a compreenderem o impacto do tempo nos investimentos e aplicar uma regra de negócio que valida se um cenário simulado atinge ou não uma meta financeira preestabelecida.

## 🚀 Funcionalidades
* **Validação de Entradas:** Impede que valores negativos sejam inseridos para capital, taxa de juros ou tempo.
* **Cálculo de Juros Compostos Iterativo:** Simula a evolução mês a mês do patrimônio.
* **Regra de Negócio (Análise de Viabilidade):** Compara o montante final obtido com uma meta financeira desejada e retorna se o objetivo foi **ALCANÇADO** ou **NÃO ALCANÇADO**.
* **Histórico Detalhado:** Retorna uma lista com a evolução do saldo mês a mês.

## 🛠️ Estrutura de Dados Utilizada
O script foi desenvolvido utilizando estruturas de dados nativas do Python para garantir leveza e portabilidade:
* **Listas (Lists):** Utilizadas para armazenar e organizar o histórico de evolução do saldo a cada mês simulado.
* **Dicionários (Dictionaries):** Utilizados para estruturar o retorno da função principal, encapsulando múltiplos tipos de dados (status, montante final, histórico e mensagens da regra de negócio) em um único objeto de fácil leitura.

## 💻 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina. Você pode verificar executando:
```bash
python --version
```

### Instruções de Execução
1. Baixe o arquivo `script.py` deste repositório.
2. Abra o terminal na pasta onde o arquivo foi salvo.
3. Execute o comando:
```bash
python script.py
```

---

## 🔬 Testes Práticos Realizados

### Cenário 1: Meta Alcançada 🎉
* **Investimento Inicial:** R$ 1.000,00
* **Taxa Mensal:** 2% (0.02)
* **Período:** 12 meses
* **Meta Desejada:** R$ 1.200,00
* **Resultado:** O montante final acumulado é de **R$ 1.268,24**. A meta foi **ALCANÇADA**.

### Cenário 2: Meta Não Alcançada ❌
* **Investimento Inicial:** R$ 500,00
* **Taxa Mensal:** 1% (0.01)
* **Período:** 6 meses
* **Meta Desejada:** R$ 600,00
* **Resultado:** O montante final acumulado é de **R$ 531,52**. A meta **NÃO FOI ALCANÇADA**.
