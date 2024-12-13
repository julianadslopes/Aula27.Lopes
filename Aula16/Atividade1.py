import polars as pl
import os
from datetime import datetime

os.system("cls")

ENDERECO_DADOS = r'./dados/'

try:
    # Marcar a hora de início
    hora_inicio = datetime.now()

    # Carregando o arquivo CSV
    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='iso-8859-1')

    # Exibindo os dados
    df_dados_lazy = df_dados.lazy()

    # Filtrando, agrupando e calculando o total de vendas por método de pagamento
    df_dados_lazy = (
        df_dados_lazy
        .filter(pl.col('regiao') == "SP")
        .select(['produto', 'preco', 'quantidade', 'forma_pagamento'])
        .group_by('forma_pagamento')
        .agg((pl.col('quantidade') * pl.col('preco')).sum().alias('total'))
    )
   
    # Coletar os dados após a execução
    df_bf = df_dados_lazy.collect()

    # Exibir os dados
    print(df_bf)

    # Marcar a hora de término
    hora_fim = datetime.now()

    print(f'Tempo de execução: {hora_fim - hora_inicio}')

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')