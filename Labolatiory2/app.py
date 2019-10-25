from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
import json
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text, CheckConstraint, Sequence, Float, UniqueConstraint
from sqlalchemy.orm import relationship
import datetime
from forms.reposytory_form import CreateReposytory, EditReposytory
from forms.project_form import CreateProject, EditProject
from forms.user_form import CreateUser, EditUser
from forms.file_form import CreateFile, EditFile
import plotly
import plotly.graph_objs as go

app = Flask(__name__)
app.secret_key = 'key'



ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost/Joseph'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qexacebxlyoflv:7f1848d692d8a690603199584eaf0f697e63459f365c69074da6ec8ca508e9fc@ec2-107-21-126-201.compute-1.amazonaws.com:5432/ddj3djvlda7rga'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ormUsers(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq', start=1, increment=1), primary_key=True)
    login = Column(String(30), UniqueConstraint(name = 'users_login_key') ,nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), UniqueConstraint(name = 'users_email_key') ,nullable=False)
    lastname = Column(String(30))
    firstname = Column(String(30))
    created = Column(DateTime, default=datetime.datetime.now())
    userRelationShip = relationship("ormReposytoty", back_populates="user_Relation_Ship")


class ormReposytoty(db.Model):
    __tablename__ = 'reposytoty'
    id = Column(Integer, Sequence('reposytoty_id_seq', start=1, increment=1), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now())
    countofprojects = Column(Integer, CheckConstraint('countofprojects >= 0'), nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_Relation_Ship = relationship("ormUsers", back_populates="userRelationShip")
    reposytotyRelationShip = relationship("ormProject", back_populates="reposytoty_Relation_Ship")

class ormProject(db.Model):
    __tablename__ = 'project'
    id = Column(Integer, Sequence('project_id_seq', start=1, increment=1), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now())
    countoffiles = Column(Integer, CheckConstraint('countoffiles >= 0'), nullable=False, default=0)
    reposytoty_id = Column(Integer, ForeignKey('reposytoty.id'))
    reposytoty_Relation_Ship = relationship("ormReposytoty", back_populates="reposytotyRelationShip")
    fileRelationShip = relationship("ormFiles", back_populates="file_Relation_Ship")


class ormFiles(db.Model):
    __tablename__ = 'files'
    id = Column(Integer, Sequence('files_id_seq', start=1, increment=1), primary_key=True)
    name = Column(String(30), nullable=False)
    file_text = Column(Text)
    expansion = Column(String(10), nullable=False)
    versions = Column(String(30), nullable=False, default='1.0')
    created = Column(DateTime, default=datetime.datetime.now())
    rating = Column(Float)
    project_id = Column(Integer, ForeignKey('project.id'))
    file_Relation_Ship = relationship("ormProject", back_populates="fileRelationShip")

@app.route('/')
def hello_world():
    text = ""
    return render_template('index.html', action="/")

@app.route('/all/user')
def all_user():
    name = "user"
    user_db = db.session.query(ormUsers).all()
    user = []
    for row in user_db:
        user.append({"id": row.id, "login": row.login, "password": row.password, "email": row.email,
                     "lastname": row.lastname, "firstname": row.firstname, "created": row.created})
    return render_template('allUser.html', name=name, users=user, action="/all/user")

@app.route('/all/reposytory')
def all_reposytory():
    name = "reposytory"
    reposytory_db = db.session.query(ormReposytoty).all()
    reposytory = []
    for row in reposytory_db:
        reposytory.append({"id": row.id, "name": row.name, "description": row.description, "created": row.created,
                           "countofprojects": row.countofprojects, "user_id": row.user_id})
    return render_template('allReposytory.html', name=name, reposytory=reposytory, action="/all/reposytory")

@app.route('/all/project')
def all_project():
    name = "project"
    project_db = db.session.query(ormProject).all()
    project = []
    for row in project_db:
        project.append({"id": row.id, "name": row.name, "description": row.description, "created": row.created,
                        "countoffiles": row.countoffiles, "reposytoty_id": row.reposytoty_id})
    return render_template('allProject.html', name=name, project=project, action="/all/project")

@app.route('/all/file')
def all_file():
    name = "file"
    file_db = db.session.query(ormFiles).all()
    file = []
    for row in file_db:
        file.append({"id": row.id, "name": row.name, "file_text": row.file_text, "expansion": row.expansion, "versions": row.versions,
                     "created": row.created, "rating": row.rating, "project_id": row.project_id})
    return render_template('allFile.html', name=name, file=file, action="/all/file")


@app.route('/create/user', methods=['GET', 'POST'])
def create_user():
    form = CreateUser()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_user.html', form=form, form_name="New user", action="create/user")
        else:

            ids = db.session.query(ormUsers).all()
            check = True
            for row in ids:
                if row.login == form.login.data:
                    check = False

            new_var = ormUsers(

                login=form.login.data,
                password=form.password.data,
                email=form.email.data,
                lastname=form.lastname.data,
                firstname=form.firstname.data,

            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_user'))

    return render_template('create_user.html', form=form, form_name="New user", action="create/user")

@app.route('/create/reposytory', methods=['GET', 'POST'])
def create_reposytory():
    form = CreateReposytory()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_reposytory.html', form=form, form_name="New reposytory", action="create/reposytory")
        else:

            ids = db.session.query(ormUsers).all()
            check = False
            for row in ids:
                if row.id == form.user_id.data:
                    check = True

            new_var = ormReposytoty(

                name=form.name.data,
                description=form.description.data,
                countofprojects=form.countofprojects.data,
                user_id=form.user_id.data
            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_reposytory'))

    return render_template('create_reposytory.html', form=form, form_name="New reposytory", action="create/reposytory")

@app.route('/create/project', methods=['GET', 'POST'])
def create_project():
    form = CreateProject()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_project.html', form=form, form_name="New project", action="create/project")
        else:

            ids = db.session.query(ormReposytoty).all()
            check = False
            for row in ids:
                if row.id == form.reposytoty_id.data:
                    check = True

            new_var = ormProject(

                name=form.name.data,
                description=form.description.data,
                countoffiles=form.countoffiles.data,
                reposytoty_id=form.reposytoty_id.data
            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_project'))

    return render_template('create_project.html', form=form, form_name="New project", action="create/project")

@app.route('/create/file', methods=['GET', 'POST'])
def create_file():
    form = CreateFile()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_file.html', form=form, form_name="New file", action="create/file")
        else:

            ids = db.session.query(ormProject).all()
            check = False
            for row in ids:
                if row.id == form.project_id.data:
                    check = True

            new_var = ormFiles(

                name=form.name.data,
                file_text=form.file_text.data,
                expansion=form.expansion.data,
                versions=form.versions.data,
                rating=form.rating.data,
                project_id=form.project_id.data
            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_file'))

    return render_template('create_file.html', form=form, form_name="New file", action="create/file")


@app.route('/delete/user', methods=['GET'])
def delete_user():
    id = request.args.get('id')

    result = db.session.query(ormUsers).filter(ormUsers.id == id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_user'))

@app.route('/delete/reposytory', methods=['GET'])
def delete_reposytory():
    id = request.args.get('id')

    result = db.session.query(ormReposytoty).filter(ormReposytoty.id == id).one()

    # db.session.delete(result)
    #
    # result = db.session.query(ormProject).filter(ormProject.reposytoty_id == id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_reposytory'))

@app.route('/delete/project', methods=['GET'])
def delete_project():
    id = request.args.get('id')

    result = db.session.query(ormProject).filter(ormProject.id == id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_project'))

@app.route('/delete/file', methods=['GET'])
def delete_file():
    id = request.args.get('id')

    result = db.session.query(ormFiles).filter(ormFiles.id == id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_file'))


@app.route('/edit/user', methods=['GET', 'POST'])
def edit_user():
    form = EditUser()
    id = request.args.get('id')
    if request.method == 'GET':

        users = db.session.query(ormUsers).filter(ormUsers.id == id).one()

        form.login.data = users.login
        form.password.data = users.password
        form.email.data = users.email
        form.lastname.data = users.lastname
        form.firstname.data = users.firstname

        return render_template('edit_user.html', form=form, form_name="Edit user",
                               action="edit/user?id=" + id)


    else:

        if form.validate() == False:
            return render_template('edit_user.html', form=form, form_name="Edit user", action="edit/user")
        else:

            # find user
            var = db.session.query(ormUsers).filter(ormUsers.id == id).one()
            print(var)

            # update fields from form data

            var.login = form.login.data
            var.password = form.password.data
            var.email = form.email.data
            var.lastname = form.lastname.data
            var.firstname = form.firstname.data
            db.session.commit()

            return redirect(url_for('all_user'))

@app.route('/edit/reposytory', methods=['GET', 'POST'])
def edit_reposytory():
    form = EditReposytory()
    id = request.args.get('id')
    if request.method == 'GET':

        reposytory = db.session.query(ormReposytoty).filter(ormReposytoty.id == id).one()

        form.name.data = reposytory.name
        form.description.data = reposytory.description
        form.countofprojects.data = reposytory.countofprojects

        return render_template('edit_reposytory.html', form=form, form_name="Edit reposytory",
                               action="edit/reposytory?id=" + id)


    else:

        if form.validate() == False:
            return render_template('edit_reposytory.html', form=form, form_name="Edit reposytory", action="edit/reposytory")
        else:

            # find user
            var = db.session.query(ormReposytoty).filter(ormReposytoty.id == id).one()
            print(var)

            # update fields from form data

            var.name = form.name.data
            var.description = form.description.data
            var.countofprojects = form.countofprojects.data
            db.session.commit()

            return redirect(url_for('all_reposytory'))

@app.route('/edit/project', methods=['GET', 'POST'])
def edit_project():
    form = EditProject()
    id = request.args.get('id')
    if request.method == 'GET':

        project = db.session.query(ormProject).filter(ormProject.id == id).one()

        form.name.data = project.name
        form.description.data = project.description
        form.countoffiles.data = project.countoffiles

        return render_template('edit_project.html', form=form, form_name="Edit project",
                               action="edit/project?id=" + id)


    else:

        if form.validate() == False:
            return render_template('edit_project.html', form=form, form_name="Edit project", action="edit/project")
        else:

            # find user
            var = db.session.query(ormProject).filter(ormProject.id == id).one()
            print(var)

            # update fields from form data

            var.name = form.name.data
            var.description = form.description.data
            var.countoffiles = form.countoffiles.data
            db.session.commit()

            return redirect(url_for('all_project'))

@app.route('/edit/file', methods=['GET', 'POST'])
def edit_file():
    form = EditFile()
    id = request.args.get('id')
    if request.method == 'GET':

        file = db.session.query(ormFiles).filter(ormFiles.id == id).one()

        form.name.data = file.name
        form.file_text.data = file.file_text
        form.versions.data = file.versions
        form.rating.data = file.rating

        return render_template('edit_file.html', form=form, form_name="Edit file",
                               action="edit/file?id=" + id)


    else:

        if form.validate() == False:
            return render_template('edit_file.html', form=form, form_name="Edit file", action="edit/file")
        else:

            # find user
            var = db.session.query(ormFiles).filter(ormFiles.id == id).one()
            print(var)

            # update fields from form data

            var.name = form.name.data
            var.file_text = form.file_text.data
            var.versions = form.versions.data
            var.rating = form.rating.data
            db.session.commit()

            return redirect(url_for('all_file'))

@app.route('/dashboard')
def dashboard():
    query1 = (
        db.session.query(
            func.count(),
            ormFiles.expansion
        ).group_by(ormFiles.expansion)
    ).all()

    query = (
        db.session.query(
            func.count(ormUsers.id),
            ormUsers.created
        ).group_by(ormUsers.created)
    ).all()

    dates, counts = zip(*query)
    bar = go.Bar(
        x=counts,
        y=dates
    )

    skills, user_count = zip(*query1)
    pie = go.Pie(
        labels=user_count,
        values=skills
    )
    print(dates, counts)
    print(skills, user_count)

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)



if __name__ == '__main__':
    app.run()
