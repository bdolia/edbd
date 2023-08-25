import edbd

from flask import Flask, request, render_template, redirect, url_for, session
from waitress import serve
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)

# The maximum number of items the session stores
# before it starts deleting some, default 500
app.config['SESSION_FILE_THRESHOLD'] = 100
app.config['SECRET_KEY'] = 'bbdfbf6e48473915872501ffff519be4aba3e2bf3a3aaa0f'
sess = Session()
sess.init_app(app)


@app.route('/encrypt', methods=('GET', 'POST'))
def encrypt():
    text = []
    if session['saved_key']:
        default_key_value = session['saved_key']
    else:
        default_key_value = ""
    if request.method == 'POST':
        if request.form['key']:
            key = request.form['key']
        else:
            key = default_key_value
        session['saved_key'] = key
        content = request.form['content']
        e = edbd.edbd(key, content)
        e.encrypt_text()
        text.append(e.return_encrypted_text())
        return redirect(url_for('result', text=text))
    return render_template('ed.html', default_key_value=default_key_value, current_procedure="Encrypting")


@app.route('/decrypt', methods=('GET', 'POST'))
def decrypt():
    text = []
    if session['saved_key']:
        default_key_value = session['saved_key']
    else:
        default_key_value = ""
    if request.method == 'POST':
        if request.form['key']:
            key = request.form['key']
        else:
            key = default_key_value
        session['saved_key'] = key
        content = request.form['content']
        e = edbd.edbd(key, content)
        e.decrypt_text()
        text.append(e.return_decrypted_text())
        return redirect(url_for('result', text=text))
    return render_template('ed.html', default_key_value=default_key_value, current_procedure="Decrypting")


@app.route('/')
def index():
    session['saved_key'] = ""
    return render_template('index.html')


@app.route('/result')
def result():
    text = request.args['text']
    return render_template('result.html', text=text)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=80)
