import pymysql as mysql

def connection():
    db=mysql.connect(host="localhost",user="root",password="1234",port=3306,db="resume")
    cmd=db.cursor()
    return db,cmd


# if __name__ =='__main__':
#     print(connection())    