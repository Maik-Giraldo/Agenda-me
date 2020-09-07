from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'agendame'

# Ruta de registro de usuario
@app.route('/registro')
def registro():
    


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
