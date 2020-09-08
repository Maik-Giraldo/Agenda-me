from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'agendame'

db = MySQL(app)

# Ruta de registro de usuario
@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/agregar', methods = ['POST'])
def agregar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        contraseña = request.form['contraseña']
        contraseña2 = request.form['contraseña2']
        if contraseña == contraseña2:
            curs = db.connection.cursor()
            curs.execute('INSERT INTO usuarios(usuario, nombre, apellidos, contraseña) VALUES (%s, %s, %s, %s)',
            (usuario, nombre, apellidos, contraseña))
            db.connection.commit()

            return redirect(url_for('registro'))
        else:
            return 'Las contraseñas no coinciden, intentalo de nuevo'



if __name__ == '__main__':
    app.run(port = 3000, debug = True)
