#impoting libraries
from tkinter import *
import mysql.connector
from datetime import datetime
import csv

#generating the tc of student
def gentc():
    gtc=Tk()
    gtc.geometry('720x780')
    gtc.resizable(height=False,width=False)
    f6=Frame(gtc,borderwidth=6,relief=SUNKEN,bg='light yellow')
    f6.pack(fill=BOTH,expand=True)
    #Label(f6,font=(2),bg='light yellow').pack()
    Label(f6,text='School Of Excellence',font=('French Script MT',55),bg='light yellow').pack()
    Label(f6,text='Sec-23,Rohini,New Delhi-86',font=('French Script MT',30),bg='light yellow').pack()
    #Label(f6,font=),bg='light yellow').pack()
    Label(f6,text='Transfer Certificate',font=('Ananda Black Personal Use',40,'underline'),bg='light yellow').pack()

    identity=id10.get()
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='school2') 
    mycur=mydb.cursor()
    mycur.execute('select * from maindata')
    mydata=mycur.fetchall()
    d=[]
    for i in mydata:
        j=list(i)
        d.append(j)
    #print(d)
    val=0
    if identity.isdigit():
        for i in d:
            if i[0]==int(identity):
                val=1
                Label(f6,text='This is to cerify that '+str(i[1])+' was admitted into ',font=('Google Sans',20),bg='light yellow').pack(anchor='nw')
                Label(f6,text='School Of Excellence, Sec-23, Rohini in 9th standard ',font=('Google Sans',20),bg='light yellow').pack(anchor='nw')
                Label(f6,text='and left on '+str(datetime.now().date())+' with a Good character.',font=('Google Sans',20),bg='light yellow').pack(anchor='nw')
                Label(f6,text='He/She was reading in the 12th Standard.',font=('Google Sans',20),bg='light yellow').pack(anchor='nw')
                Label(f6,text='Dated: '+str(datetime.now().date()),font=('Google Sans',20),bg='light yellow').pack(side=BOTTOM,anchor='nw')
                Label(f6,text='SCHOOL OF EXCELLENCE, SEC-23',font=('Google Sans',20),bg='light yellow').pack(side=BOTTOM,anchor='ne')

                break
    elif identity.isalpha():
        val=2
    else:
        val=3 

    if val==0:
        Label(f6,text='Data not found !',font=('Google Sans',20,),bg='light yellow',fg='red').pack(anchor='nw')
    elif val==2:    
        Label(f6,text='Student Roll No. is a number! ',font=('Google Sans',20,),bg='light yellow',fg='red').pack(anchor='nw')
    elif val==3:
        Label(f6,text='Please enter only a number! ',font=('Google Sans',20,),bg='light yellow',fg='red').pack(anchor='nw')
    gtc.mainloop()
#command to update a specific record of student
def updatecmd(q,first,roll):
    mydb10=mysql.connector.connect(user='root',host='localhost',passwd='1413342',database='school2')
    mycur=mydb10.cursor()
    if q=='name':
        query="update maindata set Name='{0}' where rollno={1}".format(first,roll)
    if q=='mobileno':
        first=int(first)
        query="update maindata set Phone={0} where rollno={1}".format(first,roll)
    if q=='emailid':
        query="update maindata set Email='{0}' where rollno={1}".format(first,roll)
    mycur.execute(query)
    mydb10.commit()

#to update the name in database
def updatename():
    rolly=rolli.get()
    namy=nami.get()
    updatecmd('name',namy,rolly)
    Label(f17,text='Record updated!',font=('Google Sans',15),bg='light green').grid(sticky=W)

#to update the mobile no. in database
def updatemobile():
    rolly=rolli.get()
    moby=mobi.get()
    updatecmd('mobileno',moby,rolly)
    Label(f17,text='Record updated!',font=('Google Sans',15),bg='light green').grid(sticky=W)

#to update the email ID in database
def updatemail():
    rolly=rolli.get()
    emmy=emmi.get()
    updatecmd('emailid',emmy,rolly)
    Label(f17,text='Record updated!',font=('Google Sans',15),bg='light green').grid(sticky=W)

#to update name using Student Roll No.
def un():
    unt=Tk()
    unt.geometry('1132x657')
    global f17
    f17=Frame(unt,bg='light green',borderwidth=6,relief=SUNKEN)
    f17.pack(fill=BOTH,expand=True)
    Label(f17,text='Enter the Student Roll No. and new name below:-',font=('Google Sans',15),bg='light green').grid(row=0, column=0, columnspan=2, sticky=W)
    Label(f17, text='Student Roll No.:', font=('Google Sans', 15), bg='light green').grid(row=1, column=0, sticky=W)
    global rolli
    rolli=Entry(f17)
    rolli.grid(row=1, column=1, sticky=W)
    Label(f17, text='New name:', font=('Google Sans', 15), bg='light green').grid(row=2, column=0, sticky=W)
    global nami
    nami=Entry(f17)
    nami.grid(row=2, column=1, sticky=W)
    Button(f17,text='Update!',bg='green',fg='light green',command=updatename,font=('Google Sans',10,'bold')).grid(row=3, column=0, sticky=W)
    unt.mainloop()

#to update mobile no. using Student Roll No.
def umn():
    unt=Tk()
    unt.geometry('1132x657')
    global f17
    f17=Frame(unt,bg='light green',borderwidth=6,relief=SUNKEN)
    f17.pack(fill=BOTH,expand=True)
    Label(f17,text='Enter the Student Roll No. and new mobile no. below:-',font=('Google Sans',15),bg='light green').grid(row=0, column=0, columnspan=2, sticky=W)
    Label(f17, text='Student Roll No.:', font=('Google Sans', 15), bg='light green').grid(row=1, column=0, sticky=W)
    global rolli
    rolli=Entry(f17)
    rolli.grid(row=1, column=1, sticky=W)
    Label(f17, text='New mobile no.:', font=('Google Sans', 15), bg='light green').grid(row=2, column=0, sticky=W)
    global mobi
    mobi=Entry(f17)
    mobi.grid(row=2, column=1, sticky=W)
    Button(f17,text='Update!',bg='green',fg='light green',command=updatemobile,font=('Google Sans',10,'bold')).grid(row=3, column=0, sticky=W)
    unt.mainloop()

#to update email ID using Student Roll No.
def uei():
    unt=Tk()
    unt.geometry('1132x657')
    global f17
    f17=Frame(unt,bg='light green',borderwidth=6,relief=SUNKEN)
    f17.pack(fill=BOTH,expand=True)
    Label(f17,text='Enter the Student Roll No. and new Email ID below:-',font=('Google Sans',15),bg='light green').grid(row=0, column=0, columnspan=2, sticky=W)
    Label(f17, text='Student Roll No.:', font=('Google Sans', 15), bg='light green').grid(row=1, column=0, sticky=W)
    global rolli
    rolli=Entry(f17)
    rolli.grid(row=1, column=1, sticky=W)
    Label(f17, text='New Email ID:', font=('Google Sans', 15), bg='light green').grid(row=2, column=0, sticky=W)
    global emmi
    emmi=Entry(f17)
    emmi.grid(row=2, column=1, sticky=W)
    Button(f17,text='Update!',bg='green',fg='light green',command=updatemail,font=('Google Sans',10,'bold')).grid(row=3, column=0, sticky=W)
    unt.mainloop()

#to show all the table data in a new window
def getall():
    
    mydb4=mysql.connector.connect(user='root',host='localhost',passwd='1413342',database='school2')
    mycur=mydb4.cursor()
    mycur.execute('select * from maindata')
    x=mycur.fetchall()
    with open('exported_data.csv',mode='w') as csso:
        csv_writer=csv.writer(csso)
        for i in x:
            csv_writer.writerow(list(i))
            
    gta=Tk()
    gta.geometry('500x100')
    f20=Frame(gta,borderwidth=6,relief=SUNKEN,bg='light green')
    f20.pack(fill=BOTH,expand=True)
    Label(f20,text='Data Export in the current folder!',font=('Google Sans',20),fg='green',bg='light green').pack(anchor='nw')         
    gta.mainloop()
    
#to get the student roll no.
def getid():
    global identity
    identity=id.get()
    #identity=eval(identity)
    getinfo()

#interface to take the input of data
def entdata():
    
    ed=Tk()

    ed.geometry('1132x657')
    global f10
    global ro
    global na
    global ph
    global em
    f10 = Frame(ed, borderwidth=6, relief='sunken', bg='light grey')
    f10.pack(fill=BOTH, expand=True)
    Label(f10, text='Enter the Details below of a student below to add it in the class database:', bg='light grey',font=('Google Sans', 15)).grid(row=0, column=0, columnspan=2, sticky=W)
    Label(f10, text='Roll No.: ', font=('Google Sans', 15), bg='light grey').grid(row=1, column=0, sticky=W)
    ro=Entry(f10)
    ro.grid(row=1, column=1, sticky=W)
    Label(f10, text='Name: ', font=('Google Sans', 15), bg='light grey').grid(row=2, column=0, sticky=W)
    na=Entry(f10)
    na.grid(row=2, column=1, sticky=W)
    Label(f10, text='Phone no.: ', font=('Google Sans', 15), bg='light grey').grid(row=3, column=0, sticky=W)
    ph=Entry(f10)
    ph.grid(row=3, column=1, sticky=W)
    Label(f10, text='Email Add.: ', font=('Google Sans', 15), bg='light grey').grid(row=4, column=0, sticky=W)
    em=Entry(f10)
    em.grid(row=4, column=1, sticky=W)

    #Button(f10,text='Submit!', font=('Google Sans', 15),command=dataen).grid(row=5, column=1, sticky=W)
    Button(f10, text='Submit!', font=('Google Sans', 15), command=dataen).grid(row=5, column=1, sticky=W)


    ed.mainloop()

#to get from user and insert the data in database by connector
def dataen():
    
    roll=ro.get()
    name=na.get()
    phone=ph.get()
    email=em.get()

    
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='school2') 
    mycur=mydb.cursor()
    query="insert into maindata values ({0},'{1}',{2},'{3}')".format(roll,name,phone,email)
    #print(query)
    mycur.execute(query)
    mydb.commit()

    Label(f10,text='Data Entered Successfully! ',font=('Google Sans',20,),bg='light grey',fg='green').grid(sticky=W)

#to get the data from database and show it in a interface
def getinfo():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1413342',database='school2') 
    mycur=mydb.cursor()
    mycur.execute('select * from maindata')
    mydata=mycur.fetchall()
    d=[]
    for i in mydata:
        j=list(i)
        d.append(j)
    #print(d)
    val=0
    if identity.isdigit():
        for i in d:
            if i[0]==int(identity):
                val=1
                res=Tk()
                fr1=Frame(res,bg='pink',borderwidth=6,relief=SUNKEN)
                fr1.pack(fill=BOTH,expand=True)
                Label(fr1,text='Roll No. is '+str(i[0]),bg='pink',font=('Google Sans',20)).pack(anchor='nw')
                Label(fr1,text='Name is '+str(i[1]),bg='pink',font=('Google Sans',20)).pack(anchor='nw')
                Label(fr1,text='Mobile No. is '+str(i[2]),bg='pink',font=('Google Sans',20)).pack(anchor='nw')
                Label(fr1,text='Email ID is '+str(i[3]),bg='pink',font=('Google Sans',20)).pack(anchor='nw')
                res.mainloop()
                break
    elif identity.isalpha():
        val=2
    else:
        val=3 

    if val==0:
        Label(f2,text='Data not found !',font=('Google Sans',20,),bg='light blue',fg='red').pack(anchor='nw')
    elif val==2:    
        Label(f2,text='Student roll no. is a number! ',font=('Google Sans',20,),bg='light blue',fg='red').pack(anchor='nw')
    elif val==3:
        Label(f2,text='Please enter only a number! ',font=('Google Sans',20,),bg='light blue',fg='red').pack(anchor='nw')    

#deleting a record in database by connector 
def getid2():

    id2=de.get()
    mydb2=mysql.connector.connect(user='root',host='localhost',passwd='1413342',database='school2')
    mycur2=mydb2.cursor()
    query2='delete from maindata where rollno ="{0}"'.format(id2)
    mycur2.execute(query2)
    mydb2.commit()

    Label(f2,text='Data Deleted Successfully!',font=('Google Sans',20,),bg='light blue',fg='green').pack(anchor='nw')

          
root=Tk()
root.geometry('1132x757')
root.title('Student Data Management')
f1=Frame(root,bg='pink',borderwidth=6,relief=SUNKEN)
f1.pack(fill=X)

#heading
Label(f1,text='Student Data Management System',font=('Google Sans',30),bg='pink',fg='red').pack(side=TOP)
f2=Frame(root,bg='light blue',borderwidth=6,relief=SUNKEN)
f2.pack(fill=BOTH,expand=True)

#to show number of records currently in the database
Label(f2,bg='light blue').pack()
mydb3=mysql.connector.connect(user='root',host='localhost',passwd='1413342',database='school2')
mycur=mydb3.cursor()
mycur.execute('select * from maindata')
x=mycur.fetchall()

Label(f2,text='Total records currently are: '+str(len(x)),font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw')

#to see all the records in a tabular form
Label(f2,bg='light blue').pack()
Label(f2,text='Click the button below to export all the records of the table into a csv:-',font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw',padx=6)
Button(f2,text='Click here!',font=('Google Sans',10,'bold'),command=getall,bg='blue',fg='light blue').pack(anchor='nw',pady=6,padx=10)

#to search record
Label(f2,bg='light blue').pack()
Label(f2,text='Enter the Student Roll No. of the child below to see full details:-',font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw',padx=6)
id=StringVar()
Entry(f2,textvariable=id).pack(anchor='nw',padx=10)
Button(f2,text='Search',font=('Google Sans',10,'bold'),command=getid,bg='blue',fg='light blue').pack(anchor='nw',pady=6,padx=10)

#to enter the record in database
Label(f2,bg='light blue').pack()
Label(f2,text='Click the button below to add a new student in class:-',font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw',padx=6)
Button(f2,text='Click here!',font=('Google Sans',10,'bold'),command=entdata,bg='blue',fg='light blue').pack(anchor='nw',pady=6,padx=10)

#to delete a record
Label(f2,bg='light blue').pack()
Label(f2,text='Enter the Student Roll No. of the student below to delete its record:-',font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw',padx=6)
de=Entry(f2)
de.pack(anchor='nw',padx=10)
Button(f2,text='Delete',font=('Google Sans',10,'bold'),command=getid2,bg='blue',fg='light blue').pack(anchor='nw',pady=6,padx=10)

#to generate T.C. of a student
Label(f2,bg='light blue').pack()
Label(f2,text='Enter the Student Roll No. below to generate T.C. of that student:-',font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw',padx=6)
id10=Entry(f2)
id10.pack(anchor='nw',padx=10)
Button(f2,text='Submit',bg='blue',fg='light blue',command=gentc,font=('Google Sans',10,'bold')).pack(anchor='nw',padx=10)

#to update the values of student
Label(f2,bg='light blue').pack()
Label(f2,text='To update the specific record of a student click below:-',font=('Google Sans',15),bg='light blue',fg='blue').pack(anchor='nw',padx=6)
Button(f2,text='To update the Name',command=un,font=('Google Sans',10,'bold'),bg='blue',fg='light blue').pack(side='left',anchor='ne',padx=10)
Button(f2,text='To update the Mobile No.',command=umn,font=('Google Sans',10,'bold'),bg='blue',fg='light blue').pack(side='left',anchor='ne',padx=10)
Button(f2,text='To update the Email ID',command=uei,font=('Google Sans',10,'bold'),bg='blue',fg='light blue').pack(anchor='nw',padx=10)


root.mainloop()