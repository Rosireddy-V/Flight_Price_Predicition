from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (SelectField, DateField, TimeField, IntegerField, SubmitField)
from wtforms.validators import DataRequired

train_data=pd.read_csv('data/train.csv')
val_data=pd.read_csv('data/val.csv')
x_data=pd.concat([train_data,val_data],axis=0).drop(columns=['price'])

class InputForm(FlaskForm):
    airline=SelectField(
        label='Airline',
        choices=x_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    date_of_journey=DateField(
        label='Date of journey',
        validators=[DataRequired()]
    )
    source=SelectField(
        label='Source',
        choices=x_data.source.unique().tolist(),
        validators=[DataRequired()]
    )
    destination=SelectField(
        label='destination',
        choices=x_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )
    departuretime=TimeField(
        label='Departure Time',
        validators=[DataRequired()]
    )
    arrival_time=TimeField(
        label='Arrival Time',
        validators=[DataRequired()]
    )
    duration=IntegerField(
        label='Duration',
        validators=[DataRequired()]
    )
    total_stops=IntegerField(
        label='Total Stops',
        validators=[DataRequired()]
    )
    additional_info=SelectField(
        label='Additional Info',
        choices=x_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit=SubmitField('Predict')
    