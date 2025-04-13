from dbconnection import create_db_connection
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def welcome():
    return "This is welcome page"
@app.route("/form",methods=["GET","POST"])
def form():
    try:
        if request.method=="POST":
            engine=create_db_connection(username=request.form['login'],password=request.form['password'])
            engine.connect()
            return render_template('query.html')
        return render_template('form.html')
    except Exception as e:
        return "<html><h1>❌ SQLAlchemy connection failed:</h1></html>"
@app.route("/query",methods=["GET","POST"])
def query():
    try:
        return render_template('query.html')
    except Exception as e:
        return "<html><h1>❌ SQLAlchemy connection failed:</h1></html>"

if __name__=="__main__":
    app.run(debug=True)




