# Adicionando CRUD as APIs Autor e Postagem com banco de dados
from flask import Flask, jsonify, request
from db import Autor, Postagem, app, db

# # - Criando a API Postagem

# Rota padrão - GET http://localhost:5000
@app.route('/')
def obter_postagens():
    postagens = Postagem.query.all()
    lista_de_postagem = []
    for postagem in postagens:
        postagem_atual = {}
        postagem_atual['id_postagem'] = postagem.id_postagem
        postagem_atual['titulo'] = postagem.titulo
        postagem_atual['id_autor'] = postagem.id_autor        
        lista_de_postagem.append(postagem_atual)
    return jsonify({'postagens': lista_de_postagem})

# Obter postagem por id - GET com id http://localhost:5000/postagem/1
@app.route('/<int:id_postagem>', methods=['GET'])
def obter_postagem_por_indice(id_postagem):
    postagem = Postagem.query.filter_by(id_autor=id_postagem).first()
    if not postagem:
        return jsonify(f'Postagem não encontrada!')
    postagem_atual = {}
    postagem_atual['id_postagem'] = postagem.id_postagem
    postagem_atual['titulo'] = postagem.titulo
    postagem_atual['id_autor'] = postagem.id_autor        
    return jsonify({'postagem': postagem_atual})

# Criar uma nova postagem - POST http://localhost:5000/postagem
@app.route('/', methods=['POST'])
def nova_postagem():
    nova_postagem = request.get_json()
    postagem = Postagem(titulo=nova_postagem['titulo'], id_autor=nova_postagem['id_autor'])
    db.session.add(postagem)
    db.session.commit()
    return jsonify({'mensagem': 'Postagem criada com sucesso' }, 200)


# Alterar uma postagem existente - PUT http://localhost:5000/postagem/1
@app.route('/<int:id_postagem>', methods=['PUT'])
def alterar_postagem(id_postagem):
    postagem_a_alterar = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        return jsonify({'Mensagem': 'Esta postagem não foi encontrada'})
    try:
        if postagem_a_alterar['titulo']:
            postagem.titulo = postagem_a_alterar['titulo']
    except:
        pass
    try:
        if postagem_a_alterar['id_autor']:
            postagem.id_autor = postagem_a_alterar['id_autor']
    except:
        pass

    db.session.commit()
    return jsonify({'mensagem': 'Postagem alterada com sucesso'})

# Excluir uma postagem - DELETE - https://localhost:5000/postagem/1
@app.route('/<int:id_postagem>', methods=['DELETE'])
def excluir_postagem(id_postagem):
    postagem_existente = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem_existente:
        return jsonify({'mensagem': 'Esta postagem não foi encontrada'})
    db.session.delete(postagem_existente)
    db.session.commit()
    return jsonify({'mensagem': 'Postagem excluída com sucesso'})
    
 
# # - Criando a API Autor

# Rota padrão - GET http://localhost:5000/autores
@app.route('/autores')
def obter_autores():
    autores = Autor.query.all() #Extraindo os autores do banco de dados
    # Para retornar a lista de todos os autores para alguma pessoa que está requisitando 
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
    
    return jsonify({'autores': lista_de_autores})

# Obter autor por id - GET com id http://localhost:5000/autores/1
@app.route('/autores/<int:id_autor>', methods=['GET'])
def obter_autor_por_indice(id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor não encontrado!')
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor 
    autor_atual['nome'] = autor.nome 
    autor_atual['email'] = autor.email 
    # return jsonify(f'Você buscou pelo autor: {autor_atual}')
    return jsonify({'autor': autor_atual})

# Criar uma novo autor - POST http://localhost:5000/autores
@app.route('/autores', methods=['POST'])
def novo_autor():
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])
    db.session.add(autor)
    db.session.commit()
    return jsonify({'mensagem': 'Usúario criado com sucesso'}, 200)

# Alterar uma postagem existente - PUT http://localhost:5000/autores/1
@app.route('/autores/<int:id_autor>', methods=['PUT'])
def alterar_autor(id_autor):
    usuario_a_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify({'Mensagem': 'Este usuário não foi encontrado'})
    try:
        if usuario_a_alterar['nome']:
            autor.nome = usuario_a_alterar['nome']
    except:
        pass
    try:
        if usuario_a_alterar['email']:
            autor.email = usuario_a_alterar['email']
    except:
        pass
    try: 
        if usuario_a_alterar['senha']:
            autor.senha = usuario_a_alterar['senha']
    except:
        pass

    db.session.commit()
    return jsonify({'mensagem': 'Usuário alterado com sucesso'})

# Excluir uma postagem - DELETE - https://localhost:5000/autores/1
@app.route('/autores/<int:id_autor>', methods=['DELETE'])
def excluir_autor(id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify({'mensagem': 'Este autor nào foi encontrado'})
    db.session.delete(autor_existente)
    db.session.commit()
    return jsonify({'mensagem': 'Autor excluído com sucesso'})


app.run(port=5000,host='localhost',debug=True)