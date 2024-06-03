from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, validators
from models import Producte

class ProductoForm(FlaskForm):
    nombre = StringField('Nom', [validators.DataRequired(), validators.Length(min=2, max=80)])
    descripcio = StringField('Descripció', [validators.DataRequired(), validators.Length(min=2, max=200)])

class AlbaranForm(FlaskForm):
    fecha = DateField('Data de Recepció', [validators.DataRequired()])
    proveidor = StringField('Proveïdor', [validators.DataRequired(), validators.Length(min=2, max=100)])

class LineaAlbaranForm(FlaskForm):
    producte_id = SelectField('Producte', coerce=int)
    quantitat = IntegerField('Quantitat', [validators.DataRequired()])
    preu_unitat = IntegerField('Preu per Unitat', [validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super(LineaAlbaranForm, self).__init__(*args, **kwargs)
        self.producte_id.choices = [(producte.id, producte.nom) for producte in Producte.query.all()]

class FacturaForm(FlaskForm):
    fecha = DateField('Data de Venda', [validators.DataRequired()])
    client = StringField('Client', [validators.DataRequired(), validators.Length(min=2, max=100)])

class LineaFacturaForm(FlaskForm):
    producte_id = SelectField('Producte', coerce=int)
    quantitat = IntegerField('Quantitat', [validators.DataRequired()])
    preu_unitat = IntegerField('Preu per Unitat', [validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super(LineaFacturaForm, self).__init__(*args, **kwargs)
        self.producte_id.choices = [(producte.id, producte.nom) for producte in Producte.query.all()]
