from flask import request,redirect,render_template,url_for
from app import flaskApp
from app.model import Group, Student


@flaskApp.route("/")
@flaskApp.route("/groups")
def groups():
    groups = Group.query.all()
    return render_template('listGroups.html',groups=groups) 

@flaskApp.route('/create')
def create():
    return render_template('createGroup.html')

@flaskApp.route('/submit',methods=['post'])
def submit():
     print(request.method)
     print(request.form['numberOfStudents'])
     print("Submitted!")
     return redirect(location=url_for("groups"))