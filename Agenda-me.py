from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL,MySQLdb
import bcrypt

#Configuracion con la base de datos
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_contraseña'] = ''
app.config['MYSQL_DB'] = 'agendame'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#Ruta de registro
@app.route('/agregar', methods=["GET", "POST"])
def registro():
    if request.method == 'GET':
        return render_template("registro.html")
    else:
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        contraseña = request.form['contraseña'].encode('utf-8')
        contraseña2 = request.form['contraseña2']

        #Encriptacion de contraseña
        hash_contraseña = bcrypt.hashpw(contraseña, bcrypt.gensalt())

        #Validacion de contraseñas
        if contraseña == contraseña2:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO usuarios (usuario, nombre, apellidos, contraseña) VALUES (%s,%s,%s,%s)",(usuario,nombre,apellidos,hash_contraseña,))
            mysql.connection.commit()
            session['usuario'] = request.form['usuario']
            session['nombre'] = request.form['nombre']
            return redirect(url_for('iniciar'))
        else:
            flash('Las contraseñas no coinciden, intentalo de nuevo')


# Ruta de registro
@app.route('/iniciar',methods=["GET","POST"])
def iniciar():

    # busca si el usuario esta en la bd

    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM usuarios WHERE usuario=%s",(usuario,))
        user = curl.fetchone()
        curl.close()


        if user == None:
            flash('error')
            return redirect(url_for('iniciar'))
        
        # busca si la contraseña le pertenece al usuario

        if len(user) > 0:
            if bcrypt.hashpw(contraseña, user["contraseña"].encode('utf-8')) == user["contraseña"].encode('utf-8'):
                session['usuario'] = user['usuario']
                session['nombre'] = user['nombre']
                valor= user.get('usuario')
                print(valor)
                return render_template('ver.html',lis=valor)
                

            else:
                return "error"
        
    else:
        
        
        return render_template("inicio.html")



@app.route('/bandeja')
def Index():
    return render_template('bandeja.html')

if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)