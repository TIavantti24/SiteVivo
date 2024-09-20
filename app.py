from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, static_url_path='/static')

# Rota para o formulário
@app.route('/')
def form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
