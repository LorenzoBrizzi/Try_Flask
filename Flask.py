#Prova sito fatto con Flask
#Per aprire adress web server andare su terminale da questa cartella da pycharm e inserire:
#set FLASK_APP=Flask.py
#flask run
#o posso direttamente andare su http://localhost:5000/
#ogni volta che faccio qualche modifica e voglio vederla sul mio web server devo fare CTRL+C sul terminale e poi inserire nuovamente flask run
#set FLASK_DEBUG=1 serve per farlo andare in modalita debug cosi da non dover chiudere il web server riaprirlo ogni modifica e poi flask run
#per semplificare posso inserire la funzione che ho messo a fine programma cosi da fare nel pannello direttamenre flask run



from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

