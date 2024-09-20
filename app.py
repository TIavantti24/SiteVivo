from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, static_url_path='/static')

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = '33548084'
db_name = 'banco_de_meis'

# Rota para o formulário
@app.route('/')
def form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    