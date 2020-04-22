#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, flash, redirect
from Forms import RegistrationForms, AttemptForms
import Functions
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = '4746e8af98e7eb20e34ca5d79974dbd5'
game = Functions.mastermind()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('Mastermind.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Start", methods=['GET', 'POST'])
def Start():
    form = RegistrationForms()
    if form.validate_on_submit():
        if game.find(form.username.data, form.email.data) == None:
            game.Start(form.username.data, form.email.data)
            flash(f'New Game for {form.username.data}!', 'success')
            return redirect(url_for('Play'))
        else:
            flash(f'Jogo em aberto', 'danger')
            return redirect(url_for('Start'))
    return render_template('Start.html', title='Create Account', form= form)

@app.route("/Play", methods= ['GET', 'POST'])
def Play():
    try:
        form = AttemptForms()
        if form.validate_on_submit():
            if game.find(form.username.data, form.email.data) != None:
                int(form.number.data)
                resultado = game.tentativa(form.number.data, form.username.data, form.email.data)
                flash(f'Resultado: {resultado[0]} ------ {resultado[1]}/10 Tentativas', 'success')
            else:
                flash(f'Dados invalidos', 'danger')
                return redirect(url_for('Play'))
        else:
            pass
        return render_template('Play.html', title='Play', form= form)
    except:
        logger.exception('')

@app.route("/GameRecord", methods=['GET', 'POST'])
def Record():
    try:
        data = game.record()
        return render_template('GameRecord.html', title = 'GameRecord', data = data)
    except:
        logger.exception('')

if __name__ == '__main__':
    app.run(debug = True)