from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar uma API Flask
app = Flask(__name__)

# Configuração do BD - SECRET_KEY = Acesso de autenticação único 
app.config['SECRET_KEY'] = 'FSD2323F#$!SAH'
# Definindo onde está localizado o BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# Criar uma instância de SQLAlchemy
db = SQLAlchemy(app) 
db:SQLAlchemy  # Define o tipo da variável

# Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True, autoincrement = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da tabela Autor 
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

def inicializar_banco():
    # Executando o comando para criar o Banco de Dados
    db.drop_all() # Apaga qualquer estrutura prévia que possa existir
    db.create_all() # Cria as tabelas anexadas ao db

    # Criar usuários administradores
    autor = Autor(nome='Adriano', email='adriano@gmail.com', senha='123456', admin=True)
    db.session.add(autor)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        inicializar_banco()

