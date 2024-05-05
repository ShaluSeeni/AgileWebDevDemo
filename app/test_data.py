from app import db
from app.model import *

group1 = Group()

Rose = Student (uwa_id="12345678" , name = "Rose")	
Bob = Student (uwa_id="23456789" , name = "Bob")
Mike= Student (uwa_id="34567890" , name = "Mike")
Chris =Student (uwa_id="45678901" , name = "Chris")

db.session.add_all([group1, Rose,Bob,Mike,Chris])
db.session.commit() 