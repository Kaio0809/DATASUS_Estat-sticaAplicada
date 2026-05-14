# Essa Pipeline Será usada para extração e construções dos Datasets Usados

import pandas as pd
import numpy as np

dataset_path = 'DATASUS_Estat-sticaAplicada\DENGBR25.csv'
def abre_dataset(path):
    df = pd.read_csv(path, sep=',', encoding='UTF-8')
    return df

def resumo(df:pd.DataFrame):
    print(df.info())
    print(df.head(10))



dados_dengue = abre_dataset(dataset_path)
resumo(dados_dengue)
