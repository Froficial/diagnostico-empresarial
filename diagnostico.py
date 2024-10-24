from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar o dataset
data = load_iris()
X = data.data
y = data.target

# Separar dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Criar o modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Testar o modelo
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar dataset de exemplo
data = load_iris()
X = data.data
y = data.target

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Criar e treinar o modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar o modelo
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
