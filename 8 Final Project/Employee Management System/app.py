from flask import *
from dbm import addUser,getEmp,deleteEmp,getUserById,updateEmp
import pymysql as p

def getConnect():
    return p.connect(host="localhost",user="root",password="",database="mydb")

f=Flask(__name__)

@f.route('/') #mapping
def home():
    return render_template("home.html")

@f.route('/register') #mapping
def register():
    return render_template("Register.html")

@f.route('/addUser',methods=['POST'])
def add_user():
    id=request.form['id']
    name=request.form['name']
    contact=request.form['contact']
    address=request.form['address']
    email=request.form['email']
    psw=request.form['psw']
    cnpsw=request.form['cnpsw']
    if psw==cnpsw:
        t=(id,name,contact,address,email,psw,cnpsw)
        addUser(t)
        return render_template("Login.html")
    else:
        return render_template("Register.html",error="Invalid Information")

@f.route('/login') 
def login():
    return render_template("Login.html")

@f.route('/logged',methods=['POST']) 
def log_in():
    email = request.form['email']
    psw = request.form['psw']
    db=getConnect()
    cr=db.cursor()
    sql="select * from amemp where email LIKE '{}' AND password LIKE '{}'".format(email,psw)
    cr.execute(sql)
    ln=cr.fetchall()
    if len(ln)>0:
        return render_template("welcome.html")
    else:
        return render_template("Login.html",error="Invalid Email and Password")
    db.commit()
    db.close()
    return render_template('home.html',log=ln)

@f.route('/getlist') 
def get_list():
    ul=getEmp()
    return render_template("userlist.html",ulist=ul)

@f.route('/deleteuser') 
def delete_user():
    id=request.args.get("id")
    deleteEmp(id)
    return redirect("/getlist")

@f.route('/edituser') 
def edit_user():
    id=request.args.get("id")
    u=getUserById(id)
    return render_template("updateuser.html",user=u)

@f.route('/updateEmp',methods=['POST']) 
def update_user():
    id=request.form['id']
    name=request.form['name']
    contact=request.form['contact']
    address=request.form['address']
    email=request.form['email']
    psw=request.form['psw']
    cnpsw=request.form['cnpsw']
    t=(name,contact,address,email,psw,cnpsw,id)
    updateEmp(t)
    return redirect("/getlist")  

@f.route('/logout')
def log_out():
    return render_template("home.html")

@f.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__=='__main__':
    f.run(debug=True)

