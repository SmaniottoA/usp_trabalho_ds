# -*- coding: utf-8 -*-
"""Predição Pétala

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t7MpV8E5rEb8nFcMNxJ0KaQOY-LgY4RH

Importação das bibliotecas necessárias
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

"""O Código faz download do dataset Iris diretamente da URL e faz a importação para dentro do Pandas."""

# Baixar o dataset Iris diretamente de uma URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Carregar o dataset em um DataFrame
data = pd.read_csv(url, header=None, names=columns)

"""Verificando as informações para ver se precisam ser tratados..."""

data.head()

#Verificar a presença de valores ausentes
print("Verificando valores ausentes:")
print(data.isnull().sum())  # Soma de valores ausentes por coluna

"""Gerando gráfico para entender os dados"""

import matplotlib.pyplot as plt
import seaborn as sns
# Configuração do estilo dos gráficos
sns.set(style="whitegrid")

# 1. Distribuição univariada (Histogramas)
data.hist(column=['petal_length', 'petal_width'], bins=15, figsize=(10, 5), color='skyblue', edgecolor='black')
plt.suptitle('Distribuição das Dimensões das Pétalas')
plt.show()

# 2. Distribuição bivariada (Scatter Plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='petal_length', y='petal_width', hue='species', palette='Set1')
plt.title('Comprimento vs Largura da Pétala')
plt.show()

# 3. Pairplot para análise multivariada
sns.pairplot(data, hue='species', corner=True, palette='Set2')
plt.suptitle('Relacionamento entre as Features', y=1.02)
plt.show()

# 4. Boxplots para comparação das distribuições
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='species', y='petal_length', palette='Pastel1')
plt.title('Distribuição do Comprimento da Pétala por Espécie')
plt.show()

# 5. Heatmap para correlação
plt.figure(figsize=(8, 6))
correlation = data.drop(columns='species').corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação')
plt.show()

"""De todas as informações, precisamos apenas dos dados de pétala"""

# Filtrar apenas as dimensões da pétala
X = data[['petal_length', 'petal_width']]
y = data['species']

"""Precisamos treinar o modelo e testa-lo. Para isso, precisamos separar uma porção dos dados da IRIS para teste. Utilizando a função train_test_split() para separar as features X e y de treino e teste."""

# Dividir os dados em conjuntos de treino e teste
# Separando 0.3 para uso de teste.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

"""Com o X_train, y_train separado para treinamento e X_test, y_test separado para teste. Vamos agora treinar modelo utilizando o SVM.

O *Support Vector Machine* é um algoritmo de aprendizado de máquina supervisionado usado tanto para classificação quanto para regressão, embora seja mais popular em problemas de classificação. Ele trabalha buscando o hiperplano ideal que separa as classes no espaço de características (features). Esse hiperplano é escolhido para maximizar a margem, ou seja, a distância entre o hiperplano e os pontos de dados mais próximos de cada classe
"""

# Criar e treinar o modelo SVM
model = SVC(kernel='linear', random_state=42)  # Kernel linear pode ser trocado por 'rbf', 'poly', etc.
model.fit(X_train, y_train)

"""Teste do treinamento com sua acurácia"""

# Fazer previsões
y_pred = model.predict(X_test)
# Avaliar a precisão
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo (SVM): {accuracy:.2%}")

"""Agora vamos utilizar o modelo treinado com uma hipotética especie com pétala de 1.4 de comprimento e 0.2 de largura"""

# Exemplo de previsão
especie = [[1.4, 0.2]]  # Exemplo de pétala com comprimento 1.4 e largura 0.2
especie_df = pd.DataFrame(especie, columns=['petal_length', 'petal_width'])  # Adicionar os nomes das colunas

prediction = model.predict(especie_df)
print(f"A espécie prevista para o exemplo é: {prediction[0]}")

"""# Tranformando todo o algorítimo uma classe

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, r2_score

class Modelo():

    def __init__(self, model_type):
      self.df = None
      self.model_type = model_type
      self.X_train = None
      self.X_test = None
      self.y_train = None
      self.y_test = None

    def CarregarDataset(self, path=None, url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"):
      names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']

      local = path
      if not path:
        local = url

      # Carregar o dataset em um DataFrame e devole para o df global
      self.df = pd.read_csv(local, header=None, names=names)

    # Faz o tratamento de dados...
    def TratamentoDeDados(self):
          if self.df.isnull().sum().sum() > 0:
            self.df.fillna(self.df.mean(), inplace=True)  # Substituir valores ausentes pela média
            print("Valores ausentes substituídos pela média.")
                  # Transformando y (Species) para um valor contínuo, se necessário
          pass

    # Treinamento do modelo...
    def Train(self):

            choosed_model = None
            # Filtrar apenas as dimensões da pétala
            X = self.df[['PetalLengthCm', 'PetalWidthCm']]
            y = self.df['Species']


            # Criar e treinar o modelo SVM
            if self.model_type == 'SVM':
              # Dividir os dados em conjuntos de treino e teste
              # Separando 0.3 ou seja 30% para uso de teste
              self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
              choosed_model = SVC(kernel='linear', random_state=42)
              choosed_model.fit(self.X_train, self.y_train)

            # Criar e treinar o modelo LR
            if self.model_type == 'LinearRegression':
              label_encoder = LabelEncoder()
              y = label_encoder.fit_transform(self.df['Species'])  # Converte as espécies para números
              # Separando 0.3 ou seja 30% para uso de teste
              self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
              choosed_model = LinearRegression()  # Usando LinearRegression para regressão
              choosed_model.fit(self.X_train, self.y_train)

            #Validação dos modelos:
            y_pred = choosed_model.predict(self.X_test)

            if self.model_type == 'SVM':
              accuracy = accuracy_score(self.y_test, y_pred)
              print(f"Acurácia do modelo {model}: {accuracy:.2%}")

            if self.model_type == 'LinearRegression':
              mse = mean_squared_error(self.y_test, y_pred)
              r2 = r2_score(self.y_test, y_pred)
              print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
              print(f"Coeficiente de Determinação (R²): {r2:.2f}")

            return choosed_model

    def Teste(self, model):
            """
            Avalia o desempenho do modelo treinado nos dados de teste.
            """

            y_pred = model.predict(self.X_test)

            if self.model_type == 'SVM':
              # Calcular métricas de avaliação
              acuracia = accuracy_score(self.y_test, y_pred)
              precisao = precision_score(self.y_test, y_pred, average='weighted')
              revocacao = recall_score(self.y_test, y_pred, average='weighted')
              f1 = f1_score(self.y_test, y_pred, average='weighted')
              matriz_confusao = confusion_matrix(self.y_test, y_pred)

              # Exibir resultados
              print(f"Avaliação do Modelo: {self.model_type}")
              print(f"Acurácia: {acuracia:.2f}")
              print(f"Precisão: {precisao:.2f}")
              print(f"Revocação: {revocacao:.2f}")
              print(f"F1-Score: {f1:.2f}")
              print("\nMatriz de Confusão:")
              print(matriz_confusao)
              print("\nRelatório de Classificação:")
              print(classification_report(self.y_test, y_pred))

            if self.model_type == 'LinearRegression':
                # Calcular métricas de avaliação de regressão
                mse = mean_squared_error(self.y_test, y_pred)
                r2 = r2_score(self.y_test, y_pred)

                # Exibir resultados de regressão
                print(f"Avaliação do Modelo: {self.model_type}")
                print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
                print(f"Coeficiente de Determinação (R²): {r2:.2f}")
            pass

    def IdentificarEspecie(self, data, model):

        especie_df = pd.DataFrame(data, columns=['PetalLengthCm', 'PetalWidthCm'])
        # Predição com o modelo treinado
        prediction = model.predict(especie_df)

        if self.model_type == 'SVM':
          especie_df = pd.DataFrame(data, columns=['PetalLengthCm', 'PetalWidthCm'])  # Adicionar os nomes das colunas
          print(f"A espécie prevista para o exemplo é: {prediction[0]}")

        if self.model_type == 'LinearRegression':  # Modelos de Regressão
          # Para modelos de regressão, 'prediction' será um valor contínuo, não uma classe.
          # Vamos mapear esse valor para a espécie mais próxima
          predicted_value = prediction[0]
          print(f"Valor previsto (não uma classe): {predicted_value}")
          especies = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']  # Nome das classes
          predicted_class = especies[round(predicted_value) % 3]  # Simples arredondamento (ajustar conforme necessário)
          print(f"A espécie prevista para o exemplo é: {predicted_class}")


    def CompararModelos(self):
        """
        Compara o desempenho entre o modelo de Regressão Linear e SVM (Classificação).
        """
        # Treinar e avaliar os modelos
        print(f"Treinando e avaliando o modelo de {self.model_type}...")

        # Modelo de Regressão Linear
        self.model_type = 'LinearRegression'
        modelo_regressao = self.Train()
        self.Teste(modelo_regressao)

        # Modelo SVM
        self.model_type = 'SVM'
        modelo_svm = self.Train()
        self.Teste(modelo_svm)

"""# Com a Classe criada, vamos instaciar a Classe e invocar os métodos para uso do Moldelo."""

predicao = Modelo('SVM')

predicao.CarregarDataset()

predicao.TratamentoDeDados()

modelo = predicao.Train()

predicao.Teste(modelo)

predicao.IdentificarEspecie([[1.4, 0.2]],modelo)

"""Testando com Regressão Linear"""

predicao = Modelo('LinearRegression')

predicao.CarregarDataset()

predicao.TratamentoDeDados()

modelo = predicao.Train()

predicao.Teste(modelo)

predicao.IdentificarEspecie([[1.4, 0.2]],modelo)

"""# Compara os dois modelos"""

predicao.CompararModelos()