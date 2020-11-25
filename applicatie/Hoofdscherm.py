#  hoofdscherm voor de weerstation website

from flask import Flask, render_template,  flash, redirect, request
from applicatie.forms import GrafiekForm
from applicatie.config import Config
import applicatie.lees_data as ld

import applicatie.bereken as b

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    zon_tijden = ld.geef_zon_tijden()
    zon_op = zon_tijden[0]
    zon_onder = zon_tijden[1]
    return render_template('home.html',
                           zon_op = zon_op,
                           zon_onder = zon_onder)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/grafiek2/', methods=[ 'POST','GET'])
def grafiek2():
    print('hiero')
    keuze = ['januari', 'februari', 'maart']
    # TODO lijstje met maanden afmaken
    keuze_jaren = ['2016', '2017', '2018', '2019', '2020']
    # TODO lijst met jaren ophalen uit json overzicht
    if request.method == 'POST':
        maand = request.form["maanden"]
        print ('post maand is ', maand)
    if request.method == 'GET':
        maand = request.args.get("maanden",'')
        print('get maand is ', maand)

    return render_template('grafiek2.html',
                           keuze=keuze,
                           keuze_jaren=keuze_jaren)


@app.route('/grafiek/', methods=['GET','POST'])
def grafiek():
    form = GrafiekForm()
    #if request.method == 'POST' and form.submit():
    if form.submit():
        tekst='maand ' + str(form.maand.data) + ' opgegeven voor het jaar ' + str(form.start_jaar.data)
        print(tekst)
        #grafiek_universeel(1,'jan','maximale_temp', 'maximale temperaturen')
        probeersel()
        # return redirect('/grafiek/', form=form,  tekst=tekst)
        return redirect('/grafiek/')
        # return redirect('/grafiek/')
    return render_template('grafiek.html', form=form)


def probeersel():
    print('we zitten in het probeersel')


def grafiek_universeel(maandnr, maand_naam, var_naam, naam_titel):
    data_set = b.geef_data_per_maand(maandnr, var_naam)
    # sets = []
    # for set_naam in data_set:
    #     sets.append(set_naam)
    # df = DataFrame(data_set, columns=sets)
    # plt.rcParams['figure.facecolor'] = '#FAEBD7'
    # figure = plt.Figure(figsize=(6, 5), dpi=80)
    # ax = figure.add_subplot(111)
    # chart_type = FigureCanvasTkAgg(figure, self._root)
    # chart_type.get_tk_widget().grid(row=rij, column=kolom, columnspan=6)
    # # df = df[sets].groupby('Dag').sum()
    # df.plot(kind='line', legend=True, ax=ax)  # andere kinds: bar
    # ax.set_title(naam_titel + ' ' + maand_naam)

if __name__ == '__main__':
    app.run(debug=True)
