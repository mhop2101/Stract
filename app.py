from flask import Flask, render_template, request, redirect, url_for, send_file, Response, flash
import url_helper
import scrape
import random
import time
import datetime
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

def clear():
    cache.init_app(app, config=config)
    with app.app_context():
        cache.clear()

app.secret_key = "a very secure secret_key"
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
                print(uniform_resource_locator)
                formating = url_helper.url_parser(uniform_resource_locator)
                fname = url_helper.retrieve_relevant_info(uniform_resource_locator)
                UID = "".join(random.sample(charset,16))
                fname = fname + UID + ext
                taken_time , finish_time = scrape.get_avg_time(uniform_resource_locator)
                timetwo = datetime.datetime.now()
                print(str(timetwo-timeone))
                flash("Los datos se descargarán en aproximadamente <b>{} horas {} minutos y {} segundos</b> | terminando en {} UTC-5 | <b>NO CIERRE ESTA PESTAÑA</b> | Cuando se descargue, haz click en el botón <b>Se ha descargado mi archivo</b>".format(taken_time[0],taken_time[1],taken_time[2],finish_time),
                'success')
                return redirect(url_for('time'))
                #scrape.scrape(uniform_resource_locator,formating,fname)
                #return send_file(fname,as_attachment=True)
            except:
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
    scrape.scrape(uniform_resource_locator,formating,fname)
    return send_file(fname,as_attachment=True,cache_timeout=0)

    #except:
    #    flash("Ha ocurrido un error, intenta de nuevo más tarde","danger")
    #    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
