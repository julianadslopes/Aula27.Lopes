import polars as pl
from datetime import datetime
import os

os.system('cls')

ENDERECO_DADOS = r'./dados/'

try:
    # Marcar a hora de início
    hora_inicio = datetime.now()

    # Carregando o arquivo CSV
    df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv', separator=',', encoding='iso-8859-1')

    # Exibindo os dados
    df_dados_lazy = df_dados.lazy()

    df_dados_lazy = (
        df_dados_lazy
        .group_by('regiao')
        .agg((
            pl.col('produto').value_counts().first().alias('produto_mais_vendido'),
            pl.col("forma_pagamento").value_counts().first().alias("metodo_mais_usado")))
    )

    # df_dados_lazy = (
    #     df_dados_lazy
    #     .filter(pl.col('quantidade')*pl.col('preco') > 3500)
    # )

    
    # Mostrar o plano de execução
    print("Plano de Execução:")
    print(df_dados_lazy.explain())

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