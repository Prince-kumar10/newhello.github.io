from flask import Flask,render_template,request,flash
# from sqlalchemy import SQLALchemy
app = Flask(__name__)

app.secret_key = "Prince_455666"

@app.route('/')
def Hellopeople():
    flash("What's your name ?")
    return render_template("index.html")


@app.route('/greet',methods=["POST","GET"])
def greet():
    flash("Hi " + str(request.form["name_input"])+ ", greet to see your!" )
    return render_template("index.html")

# @app.route('/hello')
# def hello ():
#     return "walcome to my second web site "

if __name__=="__main__":
    app.run(debug = True)