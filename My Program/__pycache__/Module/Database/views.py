import pymysql

mycon = pymysql.connect(host="localhost",user="root",password="",database="topsdb")
mycursor = mycon.cursor()

# -------------------------- connection done -----------------
def insertData():
    fname = input("Enter firstname : ")
    subject = input("Enter subject : ")
    city = input("Enter city : ")

    query = "insert into student (fname,subject,city) values ('%s','%s','%s') "
    args = (fname,subject,city)

    mycursor.execute(query%args)
    mycon.commit()

def getData():
    id = int(input("Enter id : "))

    query = "select * from student where id = (%s)"
    args = (id)

    mycursor.execute(query%args)
    row = mycursor.fetchone()
    print("firstname : ",row[1])
    print("subject :",row[2])

def getallData():
    query = "select * from student"

    mycursor.execute(query)
    row = mycursor.fetchall()
    print("length = ",len(row))
    print("row = ",row)
            
#insertData()
#getData()
getallData()


