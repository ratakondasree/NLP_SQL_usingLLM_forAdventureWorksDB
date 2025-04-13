from dbconnection import create_db_connection,query_answer
from flask import Flask, render_template, request,session, redirect, url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "This is welcome page"
@app.route("/form",methods=["GET","POST"])
def form():
    try:
        if request.method=="POST":
            session['login'] = request.form.get('login')
            session['password'] = request.form.get('password')
            engine=create_db_connection(username=session['login'],password=session['password'])
            engine.connect()
            print(session['login'])
            print(session['password'])
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
@app.route("/submitquery",methods=["GET","POST"])  
def submitquery():
    try:
        
        if request.method=="POST":
             stored_login = session.get("login")
             stored_password = session.get("password")
             print(stored_login,stored_password)
             query=request.form.get('query')
             result=query_answer("MyLogin","Rsri@Nov1983",query)
             
             return result 
    except Exception as e:
        return "<html><h1>❌ SQLAlchemy connection failed:</h1></html>"

if __name__=="__main__":
    app.run(debug=True)




