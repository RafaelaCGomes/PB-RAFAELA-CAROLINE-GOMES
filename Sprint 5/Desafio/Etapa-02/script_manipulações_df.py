import pandas as pd

#Ler o dataframe
caminho_arquivo = 'C:/Users/User/Desktop/Compass.uol/Sprint05/Desafio/Estoque_camarao_tratado.csv'
df = pd.read_csv(caminho_arquivo)

#Informações do df
print(df.info())

#Filtrar dados usando ao menos dois operadores lógicos: quantidade de camarão rosa > 50 e estado == 'São Paulo'
filtro = (df['Camarão Rosa (Kg)'] > 50) & (df['Estado'] == 'São Paulo') 
df_filtrado = df[filtro]
print('Filtro Camarão rosa > 50 kg e Estado == São Paulo')
print(df_filtrado.head())

#Uma função de data: Extrair o mês da 'Data de envio' 
df_filtrado['Data de envio'] = pd.to_datetime(df_filtrado['Data de envio'], errors='coerce', dayfirst=True)
df_filtrado['Mes_envio'] = df_filtrado['Data de envio'].dt.month
print('Df com seleção do mês')
print(df_filtrado.head())

#Duas funções de agregação: soma e média do camarão rosa por município
df_agrupado = df_filtrado.groupby(['Mes_envio', 'Município'], as_index=False)['Camarão Rosa (Kg)'].agg(Soma_kg_camarao_rosa='sum', Media_kg_camarao_rosa='mean')
print('Df com soma e média do camarão rosa (kg)')
print(df_agrupado.head())

#Uma função de conversão: Converter a soma do peso de camarão rosa de kg para toneladas (1t = 1000kg) 
df_agrupado['Soma_tonelada'] = df_agrupado['Soma_kg_camarao_rosa'].apply(lambda x: x / 1000)
print('Df com conversão de kh para toneladas')
print(df_agrupado.head())

#Uma função condicional: Categorizar 'soma_tonelada' como 'Alto estoque' ou 'Baixo estoque' acima de 5 toneladas de camarão. 
df_agrupado['Categoria']= df_agrupado['Soma_tonelada'].apply(lambda x: 'Alto estoque' if x > 5 else 'Baixo estoque')
print('Df com categoria de Alto e baixo estoque')
print(df_agrupado.head())

#Uma função de string: Combinar 'municipio' e Estado (SP)
df_agrupado['Município-SP'] = df_agrupado['Município'] + ' - SP '
print('Df com função string')
print(df_agrupado.head())

#Filtrar o unico estado que teve o maior número de toneladas de camarao em estoque, mostrar o valor em toneladas, a cidade, estado, classificação do estoque e o mes.
linha_max_t = df_agrupado.loc[df_agrupado['Soma_tonelada'].idxmax() ]
print('Filtro do municipio com maior toneladas de camarão em estoque')
print(linha_max_t)

#Salvando df após manipulações
df_final = pd.DataFrame(linha_max_t).transpose()
csv_final = 'Cidade_com_maior_estoque.csv'
df_final.to_csv(csv_final, index=False)
print('Salvo em .csv')

#Pergunta a ser respondida sobre o dataframe e resposta após as manipulações
pergunta_resposta = f'Pergunta: Qual o município do estado de SP, em qual mes que esse município teve o maior estoque de camarão rosa em toneladas, além disso, qual foi a media de estoque do mesmo camarão em kg e como o estoque e classificado (Alto > 5t e Baixo <5t) ? \n Resposta: O município com maior estoque de Camarão rosa foi ({linha_max_t['Município-SP']}), no mês ({linha_max_t['Mes_envio']}) teve estoque com ({linha_max_t['Soma_tonelada' ]}) toneladas, a média do mês de estoque é ({linha_max_t['Media_kg_camarao_rosa']}) e é considerado como categoria de ({linha_max_t['Categoria']})'
print(pergunta_resposta)

#Salvando a resposta em .txt
resposta_final = 'Pergunta_resposta.txt'
with open(resposta_final, 'w') as arquivo:
    arquivo.write(pergunta_resposta)
print('Resposta e pergunta salvo em .txt')