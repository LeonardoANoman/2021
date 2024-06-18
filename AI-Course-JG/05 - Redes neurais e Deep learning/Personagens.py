import tensorflow as tf
import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv("05-Redes_neurais_e_Deep_learning/personagens.csv")

print(dataset.tail())

sns.countplot(x = "classe", data=dataset)
sns.heatmap(dataset.corr(), annot=True)
X = dataset.iloc[:, 0:6].values
y = dataset.iloc[:, 6].values
y = (y == 'Bart')

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.2)

X_treinamento.shape, y_treinamento.shape

rede_neural = tf.keras.models.Sequential()
rede_neural.add(tf.keras.layers.Dense(units=4, activation='relu', input_shape=(6,)))
rede_neural.add(tf.keras.layers.Dense(units=4, activation='relu'))
rede_neural.add(tf.keras.layers.Dense(units=4, activation='relu'))
rede_neural.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

rede_neural.summary()
rede_neural.compile(optimizer='Adam', loss='binary_crossentropy', metrics = ['accuracy'])
historico = rede_neural.fit(X_treinamento, y_treinamento, epochs=50, validation_split=0.1)

historico.history.keys()

plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_accuracy'])

previsoes = rede_neural.predict(X_teste)

previsoes = (previsoes > 0.5)

accuracy_score(previsoes, y_teste)

cm = confusion_matrix(y_teste, previsoes)
