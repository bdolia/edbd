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


# @app.route('/encrypt', methods=('GET', 'POST'))
# def encrypt():
#     text = []
#     if session['saved_key']:
#         default_key_value = session['saved_key']
#     else:
#         default_key_value = ""
#     if request.method == 'POST':
#         if request.form['key']:
#             key = request.form['key']
#         else:
#             key = default_key_value
#         session['saved_key'] = key
#         content = request.form['content']
#         e = edbd.edbd(key, content)
#         e.encrypt_text()
#         text.append(e.return_encrypted_text())
#         return redirect(url_for('result', text=text))
#     return render_template('ed.html', default_key_value=default_key_value, current_procedure="encrypting =>")
#
#
# @app.route('/decrypt', methods=('GET', 'POST'))
# def decrypt():
#     text = []
#     if session['saved_key']:
#         default_key_value = session['saved_key']
#     else:
#         default_key_value = ""
#     if request.method == 'POST':
#         if request.form['key']:
#             key = request.form['key']
#         else:
#             key = default_key_value
#         session['saved_key'] = key
#         content = request.form['content']
#         e = edbd.edbd(key, content)
#         e.decrypt_text()
#         text.append(e.return_decrypted_text())
#         return redirect(url_for('result', text=text))
#     return render_template('ed.html', default_key_value=default_key_value, current_procedure="<= decrypting")


@app.route('/')
def index():
    session['saved_key'] = ""
    return render_template('ed.html')


# @app.route('/result')
# def result():
#     text = request.args['text']
#     return render_template('result.html', text=text)


@app.route('/process', methods=('GET', 'POST'))
def process():
    result = None

    if request.method == 'POST':
        if request.form['action'] == 'clear':
            session['saved_key'] = ""  # clear the saved key from session
            procedure = "<= clearing =>"
            return render_template('ed.html', default_key_value="", current_procedure=procedure, result="", key="",
                                   content="")

        key_input = request.form.get('key') or ""
        content_input = request.form['content'] or ""
        e = edbd.edbd(key_input, content_input)

        session['saved_key'] = key_input

        if request.form['action'] == 'encrypt':
            e.encrypt_text()
            result = e.return_encrypted_text()
            procedure = "encrypting =>"
        elif request.form['action'] == 'decrypt':
            e.decrypt_text()
            result = e.return_decrypted_text()
            procedure = "<= decrypting"

    return render_template('ed.html', default_key_value="", current_procedure=procedure, result=result or "",
                           key=key_input,
                           content=content_input)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
