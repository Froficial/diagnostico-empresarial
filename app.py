from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Agora estamos retornando o HTML

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem-vindo ao Diagnóstico Empresarial com IA!"

if __name__ == '__main__':
    app.run(debug=True)
