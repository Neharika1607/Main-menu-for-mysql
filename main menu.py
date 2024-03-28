import mysql.connector(host='localhost',user='root',passwd='',database='')
if conn.is_connected:
    print("successfully connected")
c1=conn.cursor()

for i in def MainMenu():
    choice=0
    while choice!=6:
        print("\n")
        print("______________________________________________")
        print("____BILLING PROCESS MANAGEMENT OF A STORE____")
        print("______________________________________________")
        print("1. Add a new Record")
        print("2. Modify Existing Record")
        print("3. Delete Existing Record")
        print("4. Search a Record")
        print("5. List all Records")
        print("6.Exit")
        choice=int(input('Enter your choice:'))
        if choice==1:
            fun1()
        elif choice==2:
            fun2()
        elif choice==3:
            fun3()
        elif choice==4:
            fun4()
        elif choice==5:
            fun5()
        elif choice==6:
            print("Software Ended")
            break

MainMenu()
