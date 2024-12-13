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
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # Totalizar por CISP
    df_total_veiculos = df_veiculos.groupby(['cisp']).sum(['roubo_veiculo', 'recuperacao_veiculos']).reset_index()

    print(df_total_veiculos.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# correlação
try:
    print ("Calculando a correlação")

    # correlação de pearson
    correlacao = np.corrcoef(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])[0,1]

    print (f'Correlação: {correlacao}')

    # plotar gráfico
    plt.scatter (df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    plt.title (f'Correlação: {correlacao}')
    plt.xlabel('Roubo de Veículos')
    plt.ylabel('Recuperação de Veículos')
    plt.show()

    
except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()
