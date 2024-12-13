#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/mort')
def mort():
    return render_template('mort.html')

@app.route('/gameover')
def gameover():
    return render_template('gameover.html')

@app.route('/ep1',methods = ['POST'])
def ep1():
    result = request.form #recupère les resultats du formulaire dans lequel on demande le nom
    n = result['nom'] #n recupère le nom
    p = result['prenom'] #p recupère le prenom
    return render_template("ep1.html", nom=n, prenom=p) #renvoie le template le nom et le prenom

@app.route('/ep2')
def ep2():
    return render_template('ep2.html')

@app.route('/ep3')
def ep3():
    return render_template('ep3.html')

@app.route('/ep4')
def ep4():
    return render_template('ep4.html')

@app.route('/ep4bis')
def ep4bis():
    return render_template('ep4bis.html')

@app.route('/ep5')
def ep5():
    return render_template('ep5.html')

@app.route('/ep5bis')
def ep5bis():
    return render_template('ep5bis.html')

@app.route('/ep6')
def ep6():
    return render_template('ep6.html')

@app.route('/eparme')
def eparme():
    return render_template('eparme.html')

@app.route('/ep6bis')
def ep6bis():
    return render_template('ep6bis.html')

@app.route('/epcollier')
def ep6collier():
    return render_template('epcollier.html')

@app.route('/ep7',methods = ['GET'])
def ep7():
    resultat = request.args #recupère les resultats du formulaire dans lequel on demande le nom

    if resultat['mdp'] == "20100": # si le mot de passe est 20100 
        page="ep7.html"         #page est egale a ep7
    else: #sinon
        page="ep6.html" #page est egale a ep6
    return render_template(page) # on renvoie la variable page
    
@app.route('/ep7bis',methods = ['GET'])
def ep7bis():
    resultat = request.args #recupère les resultats du formulaire dans lequel on demande le nom

    if resultat['mdp'] == "20100": # si le mot de passe est 20100 
        page="ep7bis.html"         #page est egale a ep7
    else: #sinon
        page="ep6bis.html" #page est egale a ep6
    return render_template(page) # on renvoie la variable page

@app.route('/ep8')
def ep8():
    return render_template('ep8.html')

@app.route('/ep9')
def ep9():
    return render_template('ep9.html')

@app.route('/ep10')
def ep10():
    return render_template('ep10.html')

@app.route('/ep11')
def ep11():
    return render_template('ep11.html')

@app.route('/ep12')
def ep12():
    return render_template('ep12.html')


app.run(debug=True)