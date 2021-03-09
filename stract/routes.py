from flask import render_template, request, redirect, url_for, send_file, flash
from stract.url_helper import url_parser, retrieve_relevant_info
from stract.scrape import scrape, get_avg_time
import random
import time
import datetime
from stract import app
from stract.cache import clear
import os

@app.route('/',methods=['GET','POST'])
def home():
    clear()
    try:
        raise e
        return render_template("index.html")
    except:
        if request.method == 'POST':
            try:
                global uniform_resource_locator
                global formating
                global fname
                timeone = datetime.datetime.now()
                ext = ".csv"
                charset = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                uniform_resource_locator = request.form.get('uniform_resource_locator')
                password = request.form.get('password')
                if password == 'Stract':
                    print(uniform_resource_locator)
                    formating = url_parser(uniform_resource_locator)
                    fname = retrieve_relevant_info(uniform_resource_locator)
                    UID = "".join(random.sample(charset,16))
                    fname = fname + UID + ext
                    taken_time , finish_time = get_avg_time(uniform_resource_locator)
                    timetwo = datetime.datetime.now()
                    print(str(timetwo-timeone))
                    if int(taken_time[1]) >= 10000000000:
                        flash("Intente con una nueva direccion, la actual contiene mas de 800 resultados","danger")
                        return render_template("index.html")
                    flash("Los datos se descargarán en aproximadamente <b>{} horas {} minutos y {} segundos</b> | terminando en {} UTC-5 | <b>NO CIERRE ESTA PESTAÑA</b> | Cuando se descargue, haz click en el botón <b>Se ha descargado mi archivo</b>".format(taken_time[0],taken_time[1],taken_time[2],finish_time),
                    'success')
                    return redirect(url_for('time'))
                    #scrape.scrape(uniform_resource_locator,formating,fname)
                    #return send_file(fname,as_attachment=True)
                else:
                    flash("Contraseña incorrecta","danger")
                    return render_template("index.html")
            except IndexError:
                flash("error","danger")
                return redirect(url_for("home"))
        try:
            if uniform_resource_locator:
                del uniform_resource_locator
                del formating
                del fname
                return render_template("index.html")
        except:
            return render_template("index.html")

@app.route("/procesando",methods=['GET','POST'])
def time():
    clear()
    if request.method == 'POST':
        return redirect(url_for('home'))
    clear()
    return render_template("time.html")

@app.route("/stract")
def stract():
    clear()
    #try:
    scrape(uniform_resource_locator,formating,fname)
    return send_file(os.getcwd()+"/stract/static/results/"+fname,as_attachment=True,cache_timeout=0)

    #except:
    #    flash("Ha ocurrido un error, intenta de nuevo más tarde","danger")
    #    return redirect(url_for("home"))
