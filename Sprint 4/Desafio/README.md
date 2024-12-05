# Resumo e Objetivo

Para o desafio da sprint 03, recebi um arquivo chamado googleplaystore.csv, onde precisei preparar o ambiente de trabalhho para trabalhar com jupyter e gerar um arquivo .IPYNB, que processa dados do datatset e gera gráficos de análises.

Para isso, foi necessário instalar a extensão do jupyter no VsCode, além de bibliotecas como Pandas e Matplotlib.

# Etapas
Para esse desafio, como o entregável é um arquivo do tipo .IPYNB, todas as etapas e itens necessários foram realizados em somente um script.

## Etapa01:
A etapa 01 do desafio foi preparar o ambiente de trabalhho com as bibliotecas e extensões necessárias.

## Script_desafio... [Etapa02:](../Desafio/Etapa-2/)
A etapa 02, possui o script onde foi realizado todo o desenvolvimento do desafio.

- Item 01: Comecei realizando a importação das bibliotecas e a leitura do arquivo googleplaystore.csv.

![Bibliotecas](../Evidencias/Import_biblio.jpg)

- Em seguida, achei necessário verificar as colunas e se continha linhas duplicadas e realizar sua 
remoção.

![Linhas_duplicadas](../Evidencias/Linhas_dupli.jpg)

- Conferi os dados das colunas e os tipos de dados de cada coluna, para saber como precisaria trabalhar com elas.

![Dados](../Evidencias/Conferencia_dados.jpg)

- Item 02: Em seguida, realizei a pesquisa e a criação do gráfico do top 5 aplicativos com maior número de instalação.

```ds_sem_dupli['Installs'] = pd.to_numeric(ds_sem_dupli['Installs'].str.replace(',', '').str.replace('+', ''), errors='coerce')

top_5_apps = ds_sem_dupli.nlargest(5, 'Installs')[['App', 'Installs']]
top_5_apps


#Dados do gráfico
Apps = top_5_apps['App']
Installs = top_5_apps['Installs']

plt.figure(figsize=(11, 9)) 

plt.bar(Apps,Installs, color='aquamarine', edgecolor='black')

plt.title ('Top 5 aplicativos mais instalados') #Titulo

plt.xlabel('Apps')
plt.ylabel('Installs')
plt.xticks(rotation=90)

plt.tight_layout() #ajusta a legenda para não sair da janela

plt.savefig('Top_5_app.jpg') #Exportação em jpg.

plt.show()


```
Tendo como gráfico:
![Top_5_apps](../Evidencias/Top_5_app.jpg)

- Item 03: Em seguida, realizei a criação do segundo gráfico.

```
freq_categoria = ds_sem_dupli['Category'].value_counts()
freq_categoria

# Adicionando um título

plt.figure(figsize=(11, 9)) 

plt.pie(freq_categoria,
        labels=freq_categoria.index, 
        autopct='( %1.1f%% )', 
        pctdistance=1.1,
        startangle=180, 
        labeldistance=1.30,
        textprops={'ha': 'center', 'va': 'center', 'fontsize': 6})

plt.title('Frequência de Categorias de Apps', loc='left', pad=44)

# Exibindo o gráfico
plt.axis('equal')  # Para garantir que o gráfico seja um círculo

plt.savefig('Frequencia_de_categorias_de_apps.jpg') #Exportação em jpg.

plt.show()

```

Tendo como resultado o gráfico:

![Frequencia_apps](../Evidencias/Frequencia_de_categorias_de_apps.jpg)

- Item 04: Para mostrar qual o aplicativo mais caro que existe no dataset, precisei converter os dados da coluna e realizar a seleção do aplicativo mais caro.
```
ds_sem_dupli['Price'] = pd.to_numeric(ds_sem_dupli['Price'].str.replace(',', '').str.replace('$', ''), errors='coerce')

app_mais_caro = ds_sem_dupli.nlargest(1, 'Price')[['App', 'Price']]
print('O aplicativo mais caro e:')
app_mais_caro

```
![App_mais_caro](../Evidencias/App_mais_caro.jpg)

- Item 05:  Para mostrar quantos os aplicativos são classificados como 'Mature 17+', realizei a contagem dos aplicativos pertencentes a classificação Mature 17+.

```
cont_apps = ds_sem_dupli['Content Rating'].value_counts().get('Mature 17+', 0)
print(f"Há {cont_apps} aplicativos classificados como 'Mature 17+' no dataset.")

```
Tendo como resultado:

![App_mature_17+](../Evidencias/Apps_mature17+.jpg)

- Item 06: Para mostrar os 10 aplicativos com maior número de reviews, precisei agrupar os nomes do aplicativos e selecionar o maior review, convverti os dados para numeric e ordenei em ordem descendente.

![Maior_review](../Evidencias/10_apps_maior_review.jpg)

- Item 07: Nesse item, realizei dois novos cálculos, um sendo os 15 aplicativos com menor tamanho e um que mostre o número total de aplicativos que são do gênero Finance.

Para os 15 aplicativos com menor tamanho usei o código.

```
ds_sem_dupli['Size'] = pd.to_numeric(ds_sem_dupli['Size'].str.replace(',', '').str.replace('M', ''), errors='coerce')


mais_leves = ds_sem_dupli.sort_values(by='Size', ascending=True).head(15)[['App', 'Size']]
mais_leves
```
Tendo como resultado:
![15_apps_menores](../Evidencias/15_apps_menores.jpg)

Para o cálculo do total de aplicativo que são do gênero Finance, usei o código:
```
apps_Finance = ds_sem_dupli['Genres'].value_counts().get('Finance', 0)
print(f"Existe {apps_Finance} aplicativos do genero 'Finance' no dataset.")
```

Tendo como resultado:
![Apps_finance](../Evidencias/Apps_finance.jpg)

- Item 08: Criei dois gráficos referente aos item realizados, sendo um dos 10 aplicativos por maior número de reviews e outro gráfico sobre os 15 aplicativos mais leves do dataset.

![Top_10_apps](../Evidencias/Top_10_apps_com_maior_avaliação.jpg)

![Top_15_apps](../Evidencias/Top_15_apps_mais_leves.jpg)












