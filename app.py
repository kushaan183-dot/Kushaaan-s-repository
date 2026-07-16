from flask import Flask, jsonify, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form.get('username')
            password = request.form.get('password')
            mydb = mysql.connector.connect(
                host="sql.freedb.tech",
                user="u_pktLem",
                password="q0qydGoWOpQK",
                database="freedb_MqwGL5sn"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM loginDetails WHERE username=%s AND password=%s", (username, password))
            account = mycursor.fetchone()
            if account:
                print("success")
                name = account[1]
                id = account[0]
                msg = "logged in successfully"
                return render_template('logout.html', msg=msg, name=name, id=id)
    else:
        msg = "invalid username or password"
        return render_template('login.html', msg=msg)
    return render_template('login.html')

@app.route('/logout')
def logout():
    name=''
    id=''
    msg="logged out successfully"
    return render_template('login.html',msg=msg,name=name,id=id)

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)