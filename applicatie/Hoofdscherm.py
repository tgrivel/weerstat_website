#  hoofdscherm voor de weerstation website

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    keuze = ['januari', 'februari', 'maart']
    #TODO lijstje met maanden afmaken
    keuze_jaren =['2016', '2017', '2018', '2019', '2020']
    #TODO lijst met jaren ophalen uit json overzicht
    return render_template('home.html',
                           keuze=keuze,
                           keuze_jaren=keuze_jaren)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
