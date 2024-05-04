from flask import request,redirect,render_template,url_for
from app import flaskApp
from app.model import Group, Student

Rose = Student (uwaId="12345678" , name = "Rose")	
Bob = Student (uwaId="23456789" , name = "Bob")
Mike= Student (uwaId="34567890" , name = "Mike")
Chris =Student (uwaId="45678901" , name = "Chris")

group1 = Group(students=[Rose,Bob,Mike,Chris])

projectGroups = [group1]
@flaskApp.route("/")
@flaskApp.route("/groups")
def groups():
    return render_template('listGroups.html',groups=projectGroups) 

@flaskApp.route('/create')
def create():
    return render_template('createGroup.html')

@flaskApp.route('/submit',methods=['post'])
def submit():
     print(request.method)
     print(request.form['numberOfStudents'])
     print("Submitted!")
     return redirect(location=url_for("groups"))