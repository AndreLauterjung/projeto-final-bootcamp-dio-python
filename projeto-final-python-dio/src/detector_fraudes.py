import pandas as pd

def analisar_transacoes_reais():
    print("--- Baixando e analisando o dataset de transações ---")
    
    # URL oficial fornecida para o projeto.
    url = "http://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
    
    # Carregando o CSV diretamente para um DataFrame do Pandas.
    # (Como o arquivo pode ser grande, vamos ler apenas as primeiras 5000 linhas para ser rápido).
    df = pd.read_csv(url, nrows=5000)
    
    print(f"Dataset carregado com sucesso! Total de linhas analisadas: {len(df)}")
    print("-" * 50)
    
    # No dataset creditcard.csv, as colunas principais são 'Time', 'Amount' (valor) e 'Class' (0 para normal, 1 para fraude).
    
    # 1. Filtrando valores zerados ou negativos no 'Amount'
    transacoes_invalidas = df[df['Amount'] <= 0]
    
    # 2. Filtrando transações marcadas como fraude ('Class' == 1)
    fraudes_detectadas = df[df['Class'] == 1]
    
    # Exibindo os resultados
    print(f"Transações com valores inválidos (Amount <= 0): {len(transacoes_invalidas)}")
    print(f"Transações fraudulentas detectadas no lote: {len(fraudes_detectadas)}")
    print("-" * 50)
    
    if not fraudes_detectadas.empty:
        print("Exemplo de transação fraudulenta:")
        print(fraudes_detectadas[['Time', 'Amount', 'Class']].head(3))

if __name__ == "__main__":
    analisar_transacoes_reais()