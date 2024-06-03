from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Albara(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proveidor = db.Column(db.String(100))
    data_recepcio = db.Column(db.Date)
    linies = db.relationship('LiniaAlbara', backref='albara', lazy=True)

class Producte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    descripcio = db.Column(db.String(200))
    preu_base = db.Column(db.Float)
    estoc = db.Column(db.Integer, default=0)
    linies_albara = db.relationship('LiniaAlbara', backref='producte', lazy=True)
    linies_factura = db.relationship('LiniaFactura', backref='producte', lazy=True)

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(100))
    data_venda = db.Column(db.Date)
    linies = db.relationship('LiniaFactura', backref='factura', lazy=True)

class LiniaAlbara(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    albara_id = db.Column(db.Integer, db.ForeignKey('albara.id'), nullable=False)
    producte_id = db.Column(db.Integer, db.ForeignKey('producte.id'), nullable=False)
    quantitat = db.Column(db.Integer)
    preu_unitat = db.Column(db.Float)

class LiniaFactura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'), nullable=False)
    producte_id = db.Column(db.Integer, db.ForeignKey('producte.id'), nullable=False)
    quantitat = db.Column(db.Integer)
    preu_unitat = db.Column(db.Float)
