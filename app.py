from flask import Flask, render_template, request, redirect

app = Flask(__name__)
#CRUD para times
Times = []

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Home')

@app.route('/times')
def list_times():
    if not Times:
        nenhum_time_cadastrado = True
    else:
        nenhum_time_cadastrado = False
    return render_template('times.html', time=Times, nenhum_time_cadastrado=nenhum_time_cadastrado, titulo = 'Times')


@app.route('/cadastrar-time', methods=['GET','POST'])
def cadastrar_time():
    if request.method == 'POST':
        nome_time = request.form['nome_time']
        quantidade_jogadores = request.form['quantidade_jogadores']
        pontos = request.form['pontos']
        Times.append({'nome': nome_time, 'quantidade': quantidade_jogadores, 'pontos': pontos})
        return redirect('/times')
    return render_template('cadastrar_time.html',titulo = 'Cadastrar Time')

@app.route('/excluir-time/<int:id>', methods=['POST'])
def excluir_time(id):
    if request.method == 'POST':
        if '_method' in request.form and request.form['_method'] == 'DELETE':
            del Times[id]
            return redirect('/times')

@app.route('/ver-time/<int:id>', methods=['GET'])
def ver_time(id):
    time = Times[id]
    return render_template('ver_time.html', time=time, titulo = 'Ver Time')

@app.route('/editar-time/<int:id>', methods=['GET','POST'])
def editar_time(id):
    if request.method == 'POST':
            if '_method' in request.form and request.form['_method'] == 'PUT':
                nome_time = request.form['nome_time']
                quantidade_jogadores = request.form['quantidade_jogadores']
                pontos = request.form['pontos']
                Times[id] = {'nome': nome_time, 'quantidade': quantidade_jogadores, 'pontos': pontos}
                return redirect('/times')
    else:
        time = Times[id]
        time['id'] = id
        return render_template('editar_time.html', time=time, titulo = 'Editar Time')


if __name__ == '__main__':
    app.run(debug=True)