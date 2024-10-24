from flask import Flask, render_template, request
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Carregar o dataset Iris e treinar o modelo
data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = RandomForestClassifier()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Capturar os dados enviados pelo formulário
        input_data = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]

        # Fazer a previsão
        prediction = model.predict([input_data])[0]
        predicted_class = data.target_names[prediction]

        # Renderizar um template com o resultado
        return render_template('result.html', predicted_class=predicted_class)
    
    except ValueError:
        # Caso haja erro na conversão dos dados, como quando o usuário insere valores não numéricos
        return "Erro: Por favor, insira valores numéricos válidos.", 400

if __name__ == '__main__':
    app.run(debug=True)
