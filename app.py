



from flask import Flask,jsonify,render_template
import os
import socket
app=Flask(__name__)

#find the hostname and machine ip


def findhostname():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

@app.route("/")
def home():
    
    return("You are highly welcome")

@app.route("/add")
def add():
    a=90
    b=80
    c=a+b
    
    return render_template('show.html',addittion=c)

@app.route("/diff")
def diff():
    a=90
    b=80
    k=a/b
    
    return render_template('show.html',division=k)

@app.route("/sub")


def subtract():
    a=90
    b=80
    f=a-b
    
    return render_template('show.html',subtract=f)

@app.route("/multiply")
def multiply():
    a=90
    b=80
    t=a*b
    
    return render_template('show.html',multiply=t)



@app.route("/score")
def calculate():
    a=40
    b=50
    result=a+b
    return render_template('show.html',finalscore=result)

@app.route("/details")
def hostme():
    myhost,myip=findhostname()
    return render_template('index.html',host=myhost,IP=myip)
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5003,host="0.0.0.0")
