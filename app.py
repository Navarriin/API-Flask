from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# Consultar(todos)
@app.route('/livros', methods=['GET']) # Rota
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET']) # Rota
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# criar
@app.route('/livros', methods=['POST']) # Rota
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Editar
@app.route('/livros/<int:id>', methods=['PUT']) # Rota
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros): 
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Deletar
@app.route('/livros/<int:id>', methods=['DELETE']) # Rota
def deletar_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)    



# starter do server    
app.run(port=5000,host='localhost',debug=True)