from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        operacao = request.form['operacao']

        operacoes = {
            'adicao': lambda x,y: x + y,
            'subtracao': lambda x,y: x - y,
            'multiplicacao': lambda x,y: x * y,
            'divisao': lambda x,y: x / y

        }

        if operacao in operacoes:
            resultado = operacoes[operacao](numero1, numero2)
        else:
            resultado = "Operação inválida"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
