from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Albara, Producte, Factura, LiniaAlbara, LiniaFactura
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/albarans', methods=['GET', 'POST'])
def gestionar_albarans():
    if request.method == 'POST':
        proveidor = request.form['proveidor']
        data_recepcio = datetime.strptime(request.form['data_recepcio'], '%Y-%m-%d')
        albara = Albara(proveidor=proveidor, data_recepcio=data_recepcio)
        db.session.add(albara)
        db.session.commit()

        for producte_id, quantitat, preu_unitat in zip(request.form.getlist('producte_id'), request.form.getlist('quantitat'), request.form.getlist('preu_unitat')):
            linia_albara = LiniaAlbara(albara_id=albara.id, producte_id=producte_id, quantitat=int(quantitat), preu_unitat=float(preu_unitat))
            producte = Producte.query.get(producte_id)
            producte.estoc += int(quantitat)
            db.session.add(linia_albara)
            db.session.add(producte)
        
        db.session.commit()
        return redirect(url_for('main.gestionar_albarans'))
    
    productes = Producte.query.all()
    albarans = Albara.query.all()
    return render_template('albarans.html', productes=productes, albarans=albarans)

@main.route('/productes', methods=['GET', 'POST'])
def gestionar_productes():
    if request.method == 'POST':
        nom = request.form['nom']
        descripcio = request.form['descripcio']
        producte = Producte(nom=nom, descripcio=descripcio)
        db.session.add(producte)
        db.session.commit()
        return redirect(url_for('main.gestionar_productes'))
    
    productes = Producte.query.all()
    return render_template('productes.html', productes=productes)

@main.route('/factures', methods=['GET', 'POST'])
def gestionar_factures():
    if request.method == 'POST':
        client = request.form['client']
        data_venda = datetime.strptime(request.form['data_venda'], '%Y-%m-%d')
        factura = Factura(client=client, data_venda=data_venda)
        db.session.add(factura)
        db.session.commit()

        for producte_id, quantitat, preu_unitat in zip(request.form.getlist('producte_id'), request.form.getlist('quantitat'), request.form.getlist('preu_unitat')):
            linia_factura = LiniaFactura(factura_id=factura.id, producte_id=producte_id, quantitat=int(quantitat), preu_unitat=float(preu_unitat))
            producte = Producte.query.get(producte_id)
            producte.estoc -= int(quantitat)
            db.session.add(linia_factura)
            db.session.add(producte)

        db.session.commit()
        return redirect(url_for('main.gestionar_factures'))
    
    productes = Producte.query.all()
    factures = Factura.query.all()
    return render_template('factures.html', productes=productes, factures=factures)