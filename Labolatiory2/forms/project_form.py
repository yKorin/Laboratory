from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators


class CreateProject(FlaskForm):
    name = StringField("Name: ", [
        validators.DataRequired("Please enter project Name.")

    ])
    description = StringField("Description: ", [
        validators.DataRequired("Please enter project Description.")

    ])

    countoffiles = IntegerField("Count Of Projects: ", [
        validators.DataRequired("Please enter project Count Of Files.")

    ])
    reposytoty_id = IntegerField("Reposytory id: ", [
        validators.DataRequired("Please enter project Reposytory id.")

    ])
    submit = SubmitField("Save")


class EditProject(FlaskForm):
    name = StringField("Name: ", [
        validators.DataRequired("Please enter project Name.")

    ])
    description = StringField("Description: ", [
        validators.DataRequired("Please enter project Description.")

    ])

    countoffiles = IntegerField("Count Of Projects: ", [
        validators.DataRequired("Please enter project Count Of Files.")

    ])

    submit = SubmitField("Save")