import mysql.connector
import csv
host = input("Enter MySQL host: ")
username = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")
database = input("Enter MySQL database name: ")
m = mysql.connector.connect(host=host,
                            username=username,
                            password=password,
                            )
x = m.cursor()
x.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print("database created if not existed\n")
m.database = database

def create_items():
    q="create table items(itemNo int,name varchar(30),purchaseRate int, quantity int, marketRate int);"
    x.execute(q)
    m.commit()

def employeedetails():
    q="create table employeedetails(eno int,name varchar(30),doj varchar(30), salary int);"
    x.execute(q)
    m.commit()

def supplierdetails():
    q="create table supplierdetails(sno int,name varchar(30),product varchar(30), quantity int);"
    x.execute(q)
    m.commit()

def transactions():
    q="create table transactions(sno int,iop int,profitgen int,sfe int);"
    x.execute(q)
    m.commit()

def tables():
    print("Have you created your tables yet?")
    n=input("YES OR NO?")
    n=n.upper()
    if (n=='YES'):
        print("OK")
    elif(n=='NO'):
        print("tables created(items,customerdetails,supplierdetails,transactions)")
        create_items()
        employeedetails()
        supplierdetails()
        transactions()
    else:
        print("INAPPROPRIATE INPUT")
tables()

print("NOTE- PLEASE ADD DATA IN YOUR TABLE BEFORE EDITING OR DELETING IT")
def add_items():
    itemNo = int(input("Enter item number"))
    name = input("Enter the name of item")
    purchaseRate = int(input("Enter the rate at which purchased"))
    quantity = int(input("enter the quantity of item"))
    marketRate = int(input("Enter the market rate"))
    q = "insert into items values({},'{}',{},{},{});".format(
        itemNo, name, purchaseRate, quantity, marketRate
    )
    x.execute(q)
    m.commit()
    print("Item Added\n")

def add_transactions():
    sno = int(input("Enter data number"))
    iop = int(input("Enter the investment made on products"))
    profitgen = int(input("Enter the profit generated from the products"))
    sfe = int(input("enter the salary of employees"))
    q = "insert into transactions values({},{},{},{});".format(
        sno, iop, profitgen, sfe
    )
    x.execute(q)
    m.commit()
    print("transactions added\n")

def add_employeedetails():
    eno = int(input("Enter employee number"))
    name = input("Enter the name of employee")
    doj = input("Enter the date of joining ")
    salary = int(input("enter the salary"))
    q = "insert into employeedetails values({},'{}',{},{});".format(
        eno, name, doj, salary
    )
    x.execute(q)
    m.commit()
    print("Employee Details added\n")

def add_supplierdetails():
    sno = int(input("Enter supplier number"))
    name = input("Enter the name of supplier")
    product = input("Enter the product ")
    quantity = int(input("enter the quantity"))
    q = "insert into supplierdetails values({},'{}','{}',{});".format(
        sno, name, product, quantity
    )
    x.execute(q)
    m.commit()
    print("supplier Details added\n")

def view_supplierdetails():
    x.execute("select * from supplierdetails")
    print("serial no, name, product, quantity")
    p = x.fetchall()
    for i in p:
        print(i)

def delete_supplierdetails():
    name = input("enter the name of the employee whose details to be deleted")
    q = "delete from supplierdetails where name='{}';".format(name)
    x.execute(q)
    m.commit()

def edit_supplierdetails():
    sno = int(input("enter supplier no."))
    q = "select * from supplierdetails where itemNo = {};".format(sno)
    x.execute(q)
    if x.fetchone():
        name = input("Enter the new name")
        x.execute(
            "update supplierdetails set name = '{}' where itemNo={};".format(name, sno)
        )
        m.commit()
        print("supplier details edited\n")
    else:
        print("suplier details not found\n")

def view_items():
    x.execute("select * from items")
    p = x.fetchall()
    print("itemNo, name, purchaseRate, quantity, marketRate")
    for i in p:
        print(i)

def view_transactions():
    x.execute("select * from transactions")
    p = x.fetchall()
    print("(serial no, investment on product, profit generated, salary for employee)")
    for i in p:
        print(i)

def view_employeedetails():
    x.execute("select * from employeedetails")
    p = x.fetchall()
    print("employee no, name, date of joining, salary")
    for i in p:
        print(i)

def delete_items():
    name = input("enter the name which product details to be deleted")
    q = "delete from items where name='{}';".format(name)
    x.execute(q)
    m.commit()

def delete_employeedetails():
    name = input("enter the name of the employee whose details to be deleted")
    q = "delete from employeedetails where name='{}';".format(name)
    x.execute(q)
    m.commit()

def delete_transactions():
    sno = input("enter the data number whose information to be deleted")
    q = "delete from transactions where sno={};".format(sno)
    x.execute(q)
    m.commit()

def edit_item():
    itemNo = int(input("enter item no."))
    q = "select * from items where itemNo = {};".format(itemNo)
    x.execute(q)
    if x.fetchone():
        name = input("Enter the new name")
        x.execute("update items set name = '{}' where itemNo={};".format(name, itemNo))
        m.commit()
        print("item edited\n")
    else:
        print("item not found\n")

def edit_employeedetails():
    eno = int(input("enter employee no."))
    q = "select * from employeedetails where eno = {};".format(eno)
    x.execute(q)
    if x.fetchone():
        name = input("Enter the new name")
        x.execute(
            "update employeedetails set name = '{}' where eno={};".format(name, eno)
        )
        m.commit()
        print("employee details edited\n")
    else:
        print("employee details not found\n")

def edit_transactions():
    sno = int(input("enter the data number"))
    q = "select * from transactions where sno = {};".format(sno)
    x.execute(q)
    if x.fetchone():
        profitgen = int(input("Enter the new profit generated"))
        x.execute(
            "update employeedetails set profitgen = {} where sno={};".format(
                profitgen, sno
            )
        )
        m.commit()
        print("transaction details edited\n")
    else:
        print("transaction details not found\n")

while 1:
    print("MENU\n")
    print("1.items")
    print("2.employee details")
    print("3.suppliers")
    print("4.transactions")
    print("5.report")
    print("6.exit\n")
    n = int(input("ENTER YOUR CHOICE"))
# items
    if n == 1:
        print("MENU\n")
        print("1.Add Items")
        print("2.Edit Items")
        print("3.Delete Items")
        print("4.View Items")
        print("5.Exit\n")
        n = int(input("Enter your choice"))
        if n == 1:
            add_items()
        elif n == 2:
            edit_item()
        elif n == 3:
            delete_items()
        elif n == 4:
            view_items()
        elif n == 5:
            break
# customers
    elif n == 2:
        print("MENU\n")
        print("1.Add employee Details")
        print("2.Edit employee Details")
        print("3.Delete employee Details")
        print("4.View employee Details")
        print("5.Exit\n")
        n = int(input("Enter your choice"))
        if n == 1:
            add_employeedetails()
        elif n == 2:
            edit_employeedetails()
        elif n == 3:
            delete_employeedetails()
        elif n == 4:
            view_employeedetails()
        elif n == 5:
            break
#suppliers
    elif n == 3:
        print("MENU\n")
        print("1.Add Suppliers Details")
        print("2.Edit Suppliers Details")
        print("3.Delete Suppliers Details")
        print("4.View Suppliers Details")
        print("5.Exit\n")
        n = int(input("Enter your choice"))
        if n == 1:
            add_supplierdetails()
        elif n == 2:
            edit_supplierdetails()
        elif n == 3:
            delete_supplierdetails()
        elif n == 4:
            view_supplierdetails()
        elif n == 5:
            break
# transactions
    elif n == 4:
        print("MENU\n")
        print("1.Add any transactions")
        print("2.Edit transactions")
        print("3.Delete transactions")
        print("4.View transactions")
        print("5.Exit\n")
        n = int(input("Enter your choice"))
        if n == 1:
            add_transactions()
        elif n == 2:
            edit_transactions()
        elif n == 3:
            delete_transactions()
        elif n == 4:
            view_transactions()
        elif n == 5:
            break
# report
    elif n == 5:
        print("MENU\n")
        print("1.Best selling item")
        print("2.Net profit")
        print("3.Exit\n")
        n = int(input("Enter your choice"))
        if n == 1:
            q="select itemNo,name,(marketRate-purchaseRate)*quantity as profit from items order by 3 desc limit 1"
            x.execute(q)
            r=x.fetchall()
            with open('inventory.csv','w+') as  f:
                for i in r:
                    print("(itemNo,name,profit)")
                    print(i)
                    f.write(str(i))
        elif n == 2:
            q="select profitgen as netprofit from transactions "
            x.execute(q)
            r=x.fetchall()
            with open('inventory.csv','w+') as  f:
                for i in r:
                    print("NET PROFIT")
                    for j in i:
                        print(j)
                        print()
                    f.write(str(i))
        elif n == 3:
            break
    elif n == 6:
        print("thankyou for using inventory management system ")
        break
    else:
        print("INAPPROPRIATE INPUT\n")