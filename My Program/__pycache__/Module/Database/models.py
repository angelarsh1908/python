import pymysql

my_con = pymysql.connect(host="localhost",user="root",password="")

mycursor = my_con.cursor()
mycursor.execute("create database topsdb")
my_con.commit() # for save

my_con = pymysql.connect(host="localhost",user="root",password="",database="topsdb")
mycursor = my_con.cursor()

mycursor.execute("create table student (id integer primary key auto_increment,fname varchar(20),subject varchar(20),city varchar(20)) ")
my_con.commit()



