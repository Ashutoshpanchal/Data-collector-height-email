from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:ashutosh@localhost/height_collector"
db=SQLAlchemy(app)



class Data(db.Model):
    _tablename_="data"
    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)



    def __init__(self,email,height):
        self.email=email
        self.height=height



@app.route("/")

def  index():
    return render_template("index.html")

@app.route("/success",methods=["POST"])

def  success():
    if  request.method=="POST":
        email=request.form["email_name"]
        height = request.form["height_name"]
        send_email(email,height)
        print(email)
        print(height)
        if db.session.query(Data).filter(Data.email==email).count()==0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template("index.html",
                                   text="email Already exits")

if __name__=="__main__":
    app.debug=True
    app.run(port=50001)