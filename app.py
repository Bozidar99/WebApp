from flask import Flask, render_template, request, redirect
from cs50 import SQL


app = Flask(__name__)

db = SQL("sqlite:///narudzbe.db")

ODJECA = [
    "Majica",
    "Hlace",
    "Trenerka",
    "Jakna",
    "Prsluk",
    "Duks"
]

@app.route("/")
def index():
    return render_template("index.html", odjeca = ODJECA)


@app.route("/spremi", methods=["POST"])
def spremi():
    
    ime = request.form.get("ime")
    prezime = request.form.get("prezime")
    grad = request.form.get("grad")
    adresa = request.form.get("adresa")
    broj_telefona = request.form.get("broj_telefona")
    odabrana_odjeca = request.form.get("odabrana_odjeca")

    
    if not ime or not prezime or not grad or not adresa or not broj_telefona or odabrana_odjeca not in ODJECA:
        return render_template("failure.html")
    

    db.execute("INSERT INTO narudzbe(ime, prezime, grad, adresa, broj_telefona, odjeca) VALUES(?, ?, ?, ?, ?, ?)", 
               ime, prezime, grad, adresa, broj_telefona, odabrana_odjeca)
    
    return render_template("success.html")    