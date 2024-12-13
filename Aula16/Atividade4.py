import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.system('cls')

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Demilitando somente as variáveis
    df_lesao_corporal = df_ocorrencias[['cisp','lesao_corp_dolosa', 'lesao_corp_culposa']]

    # Totalizar por CISP
    df_lesao_corporal_cisp = df_lesao_corporal.groupby(['cisp']).sum([['lesao_corp_dolosa', 'lesao_corp_culposa']]).reset_index()

    print(df_lesao_corporal_cisp.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# correlação
try:
    print ("Calculando a correlação")

    # correlação de pearson
    correlacao = np.corrcoef(df_lesao_corporal_cisp['lesao_corp_culposa'], df_lesao_corporal_cisp['lesao_corp_dolosa'])[0,1]

    print (f'Correlação: {correlacao}')

    # plotar gráfico
    plt.scatter (df_lesao_corporal_cisp['lesao_corp_culposa'], df_lesao_corporal_cisp['lesao_corp_dolosa'])
    plt.title (f'Correlação: {correlacao}')
    plt.xlabel('Lesão Corporal Culposa')
    plt.ylabel('Lesão Corporal Dolosa')
    plt.show()

    
except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()
