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
    print("6 exit")
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
         print("selected view all donors")
    elif(ch==3):
        print("selected search a donor")
    elif(ch==4):
        print("selected update  donor")
    elif(ch==5):
        print("selected delete donor")
    elif(ch==6):
        break