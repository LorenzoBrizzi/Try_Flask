#Prova sito fatto con Flask
#Per aprire adress web server andare su terminale da questa cartella da pycharm e inserire:
#set FLASK_APP=Flask.py
#flask run
#o posso direttamente andare su http://localhost:5000/
#ogni volta che faccio qualche modifica e voglio vederla sul mio web server devo fare CTRL+C sul terminale e poi inserire nuovamente flask run
#set FLASK_DEBUG=1 serve per farlo andare in modalita debug cosi da non dover chiudere il web server riaprirlo ogni modifica e poi flask run
#per semplificare posso inserire la funzione che ho messo a fine programma cosi da fare nel pannello direttamenre flask run



from flask import Flask
app = Flask(__name__)

@app.route("/")                                 #dopo lo shalsh si matte la pagina e se si vuole mettere la stessa funzione in piu pagine basta fare come qui aggiungendo decorators alla stessa funzione
@app.route("/home")
def home_page():
    return "<h1>Home Page</h1>"

@app.route("/about")
def About():
    return "<h2>About</h2>"





#per farlo girare in debug mode cosi per diminuire i passaggi per il web server
if __name__ == "__main__":
    app.run(debug=True)

