from sanic_wtf import SanicForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


class Payloads_JXA_Form(SanicForm):
    callback_host = StringField('Callback Host', validators=[DataRequired()])
    callback_port = IntegerField('Callback Port', validators=[DataRequired()])
    obfuscation = BooleanField('Obfuscation')
    output_directory = StringField('Output Directory', validators=[DataRequired()])
    callback_interval = IntegerField('Callback Interval', validators=[DataRequired()])
    default_tag = StringField('Default tag')
    c2_profile = SelectField('C2 Profile', coerce=str)
    submit = SubmitField('Create Payload')

