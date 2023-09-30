#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Menghubungkan SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Membuat sebuah DB
db = SQLAlchemy(app)

#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_pressed = None
    if request.form.get('button_python'):
        button_pressed = 'python'
    elif request.form.get('button_discord'):
        button_pressed = 'discord'
    elif request.form.get('button_html'):
        button_pressed = 'html'
    elif request.form.get('button_db'):
        button_pressed = 'db'
    return render_template('index.html', button_pressed=button_pressed)


if __name__ == "__main__":
    app.run(debug=True)
