import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bloodbankdb')

mycursor=mydb.cursor()
while True:
    print("\nSelect an option")
    print("1 add a donor")
    print("2 view all donors")
    print("3 search a donor")
    print("4 update  donor")
    print("5 delete  donor")
    print("6 search donor by specific letter in name ")
    print("7 exit")
    ch=int(input("select an option  : \n"))
    if (ch==1):    
        name=input("Enter the name")
        address=input("Enter address")
        phno=input("Enter the phone number")
        age=input("Enter the age")
        sex=input("Enter the sex")
        bg=input("Enter the blood group")
        sql='INSERT INTO `donor`(`name`, `address`, `phno`, `age`, `sex`, `bloodgp`) VALUES (%s,%s,%s,%s,%s,%s)'
        data=(name,address,phno,age,sex,bg)
        mycursor.execute(sql,data)
        mydb.commit()        
        print("inserted success")
    elif(ch==2):
        sql='SELECT * FROM `donor`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(ch==3):
        name=input("Enter the  name for searching the donors")
        sql="SELECT * FROM `donor` WHERE `name`='"+name+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(ch==4):
        name=input("Enter the donor name ")
        address=input("enter the address to be updated")
        phn=input("enter the phone number to be updated ")
        age=input("enter the age to be updated")
        sql="UPDATE `donor` SET `address`='"+address+"',`phno`='"+phn+"',`age`='"+age+"' WHERE `name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("updated successfully") 
    elif(ch==5):
        name=input("Enter the donor name for deletion ")
        sql="DELETE FROM `donor` WHERE `name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("deleted successfully")
    elif(ch==6):
        sl= input("Enter the letter to search the donor ")
        sql="SELECT `name`, `address`, `phno`, `age`, `sex`,`bloodgp` FROM `donor` WHERE `name` LIKE '"+sl+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(ch==7):
        break