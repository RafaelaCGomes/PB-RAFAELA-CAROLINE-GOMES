import pandas as pd

#Ler o dataset
caminho_arquivo = 'C:/Users/User/Desktop/Compass.uol/Sprint05/Desafio/Declarações_de_Estoque-Camarão_656-Sudeste-Sul(Camarao 656 sudeste-sul).csv'
ds = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')

print(ds.head())

#Verificação dos tipos de dados das colunas
print(ds.info())

#Alteração do tipo de dado da coluna 'Data de venda' para datetime.
ds['Data de envio'] = pd.to_datetime(ds['Data de envio'], errors='coerce', dayfirst=True)
print(ds.info())

#Alteração do tipo de dado das colunas de Camarão para float.
ds['Camarão Rosa (Kg)'] = pd.to_numeric(ds['Camarão Rosa (Kg)'], errors='coerce')
ds['Camarão Sete Barbas (Kg)'] = pd.to_numeric(ds['Camarão Sete Barbas (Kg)'], errors='coerce')
ds['Camarão Branco (Kg)'] = pd.to_numeric(ds['Camarão Branco (Kg)'], errors='coerce')
ds['Camarão Santana ou Vermelho (Kg)'] = pd.to_numeric(ds[ 'Camarão Santana ou Vermelho (Kg)'], errors='coerce')
ds['Camarão Barba-ruça (Kg)'] = pd.to_numeric(ds['Camarão Barba-ruça (Kg)'], errors='coerce')
print(ds.info())

#Nova verificação das colunas 
print(ds.head())

#Salvar o novo Dataframe tratado
df_tratado = 'Estoque_camarao_tratado.csv'
ds.to_csv(df_tratado, index=False)
print('Data frame salvo em .csv')