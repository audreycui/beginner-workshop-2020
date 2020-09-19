from my_app import db

class Fact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	value = db.Column(db.String(100))

class Post(db.Model): 
    id = db.Column(Db.Integer, primary_key = True)
    title = db.Column(Db.String(1000))
    description = db.Column(Db.String(1000))