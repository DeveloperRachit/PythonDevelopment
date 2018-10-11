import cx_Oracle
Con1=cx_Oracle.connect("system/mca6@localhost:1521/xe")
curl1=Con1.cursor()
curl1.execute("select * from Employee")
for result in curl1.fetchall():
        print(result)   
        Con1.commit()