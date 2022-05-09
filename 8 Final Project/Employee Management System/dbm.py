import pymysql as p

def getConnect():
    return p.connect(host="localhost",user="root",password="",database="mydb")

def addUser(t):
    db=getConnect()#connection established
    cr=db.cursor()#cursor object created
    sql="insert into amemp values(%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

    
def getEmp():
    sql="select * from amemp"
    db=getConnect()
    cr=db.cursor()
    cr.execute(sql)
    ulist=cr.fetchall()
    db.commit()
    db.close()
    return ulist

def deleteEmp(id):
    db=getConnect()#connection established
    cr=db.cursor()#cursor object created
    sql="delete from amemp where id=%s"
    cr.execute(sql,id)
    db.commit()
    db.close()

def getUserById(id):
    sql="select * from amemp where id=%s"
    db=getConnect()
    cr=db.cursor()
    cr.execute(sql,id)
    ulist=cr.fetchall()
    db.commit()
    db.close()
    return ulist[0]

def updateEmp(t):
    db=getConnect()
    cr=db.cursor()
    sql="update amemp set use name=%s,contact=%s,address=%s,email=%s,password=%s,conpassword=%s where id=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()
