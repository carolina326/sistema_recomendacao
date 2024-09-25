# -*- coding: utf-8 -*-
"""TP_Agrupamento.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11tN4FIQei6L9IZ_g1NqGURTjzZOYo6mZ
"""

#Importando
import numpy as np
from sklearn.cluster import KMeans
filmes_assistidos = np.array([
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
])

#Treinar o modelo
#Número de clusters(Grupo)
num_clusters = 2

#Inicializando o modelo
kmeans = KMeans(n_clusters=num_clusters,random_state=0,n_init=10)

#Treinando o  modelo
kmeans.fit(filmes_assistidos)

#Classificando os usuarios
grupos_indice = kmeans.predict(filmes_assistidos)

#Exibir os dados
print("Usuario pertence ao seguinte grupo:")
for i, cluster in enumerate(grupos_indice):
  print(f"Usuario {i+1} pertence ao grupo {cluster+1}")

print("\nFilmes assistidos:")
for i in range(len(filmes_assistidos)):
    assistidos = np.where(filmes_assistidos[i] == 1)[0] + 1
    print(f"Usuario {i+1} assistiu aos filmes: {assistidos}")

#Funçâo que recomenda filmes
def recomendar_filmes(filmes, filmes_assistidos, grupos_indice):

  filmes = np.array(filmes)

  #Encontrar o grupo do usuario com base em seu vetor de filmes
  usuario_id = len(filmes_assistidos)
  grupo_usuario = kmeans.predict([filmes])[0]

  #Encontrar todos os usuários no mesmo grupo
  usuarios_no_mesmo_grupo = [i for i in range(len(grupos_indice))
  if grupos_indice[i] == grupo_usuario]

  #Filmes assistidos pelos usuários no mesmo grupo
  filmes_recomendados = set()
  for usuario in usuarios_no_mesmo_grupo:
    filmes_assistidos_usuario = np.where(filmes_assistidos[usuario] == 1)[0]
    filmes_recomendados.update(filmes_assistidos_usuario)

  # Remover filmes que o usuário já assistiu
  filmes_recomendados = filmes_recomendados - set(np.where(filmes == 1)[0])

  #Ajustar os indices dos filmes recomendados (de volta para 1-based)
  filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

  return  sorted(filmes_recomendados)


# Exemplo de uso da função recomendar_filmes
filmes_assistidos_usuario = [1, 0, 1, 0] # Vetor de filmes
#assistidos (por exemplo, assistiu aos filmes 1 e 3)
filmes_recomendados = recomendar_filmes(filmes_assistidos_usuario,filmes_assistidos, grupos_indice)

print(f"\nFilmes recomendados: {filmes_recomendados}")