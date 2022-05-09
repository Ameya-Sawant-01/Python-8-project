import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='ameya')
    
def addEmp(t):
    db=getConnection()
    sql='insert into flaskpj values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAllEmp():
    db=getConnection()
    sql='select * from flaskpj'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteEmp(id):
    db=getConnection()
    sql='delete from  flaskpj where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from flaskpj where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update flaskpj set name=%s,contact=%s,email=%s,passw=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def log(t):
    db=getConnection()
    sql="select name,passw from flaskpj where name=%s and passw=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
