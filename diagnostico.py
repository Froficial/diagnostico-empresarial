from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Carregar o dataset Iris
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
predictions = model.predict(X_test)

# Exibir a acurácia e outras métricas
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
print("Classification Report:\n", classification_report(y_test, predictions))
