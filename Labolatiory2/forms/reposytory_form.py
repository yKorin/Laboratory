from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators


class CreateReposytory(FlaskForm):
    name = StringField("Name: ", [
        validators.DataRequired("Please enter reposytory Name.")

    ])
    description = StringField("Description: ", [
        validators.DataRequired("Please enter reposytory Description.")

    ])

    countofprojects = IntegerField("Count Of Projects: ", [
        validators.DataRequired("Please enter reposytory Count Of Projects.")

    ])
    user_id = IntegerField("User id: ", [
        validators.DataRequired("Please enter reposytory User id.")

    ])
    submit = SubmitField("Save")


class EditReposytory(FlaskForm):
    name = StringField("Name: ", [
        validators.DataRequired("Please enter reposytory Name.")

    ])
    description = StringField("Description: ", [
        validators.DataRequired("Please enter reposytory Description.")

    ])

    countofprojects = IntegerField("Count Of Projects: ", [
        validators.DataRequired("Please enter reposytory Count Of Projects.")

    ])

    submit = SubmitField("Save")