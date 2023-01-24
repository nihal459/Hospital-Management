from django.shortcuts import render
import mysql.connector

# Create your views here.

#home page
def home(request):
    return render(request, 'home.html')

#_______________________________________________________________________________________________________________

#DOCTOR

#doctor registration page
def registration(request):
    return render(request, 'registration.html') 

def viewappointments(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    a=str(request.session['sdocno'])
    q="select * from appoinment where doctorid='" + a + "'"
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request, 'viewappointments.html',{'drows':row, 'dname':request.session['susername']})

#doctor registration handler
def registerhandler(request):
    a=request.POST.get("name")
    b=request.POST.get("gender")
    c=request.POST.get("date")
    d=request.POST.get("specialisation")
    e=request.POST.get("district")
    f=request.POST.get("email")
    g=request.POST.get("phone")
    h=request.POST.get("username")
    i=request.POST.get("password")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="insert into doc(name,gender,dob,specialisation,district,email,phonenumber,username,password) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+i+"')"
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return render(request, 'registration.html')
    
    
 
#doctor login page 
def doctorlogin(request):
    return render(request, 'doctorlogin.html')

#doctor login handler
def loginhandler(request):
    a=request.GET.get("username")
    b=request.GET.get("pass")
    print(a)
    print(b)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from doc where username='"+a+"' and password='"+b+"'"
    mycursor.execute(q)
    row=mycursor.fetchone()
    if row!=None:
     request.session['susername']=a
     request.session['sdocno']=row[0]
     return render(request, 'doctorhome.html',{'dname':a})
    else:
     return render(request, 'doctorlogin.html',{'msg':'Invalid Credentials'})  
 
 
 
#doctor home page 
def doctorhome(request):
    return render(request, 'doctorhome.html',{'dname':request.session['susername']})  


#def approvehandler(request):
    #mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    #mycursor=mydb.cursor()
    #a=request.GET.get("approveid")
    #c="Approved"
    #d=request.session['sdocno']
    #q="update appoinment set status = '"+c+"' where patientid="+str(a) 
    #mycursor.execute(q)
    #row=mycursor.fetchone()
    #mydb.commit()
    #mydb.close()
    #return render(request, 'viewappointments.html')

    


#doctor profile page
def profile(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    s=request.session['sdocno']
    q="select * from doc where docid="+str(s)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request, 'profile.html',{'dname':request.session['susername'], 'drows':row})

#doctor profile update handler
def profileupdatehandler(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    a=request.POST.get("email")
    b=request.POST.get("phone")
    c=request.POST.get("pass")
    d=request.session['sdocno']
    q="update doc set password='"+c+"', email='"+a+"', PhoneNumber='"+b+"' where docid="+str(d)
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.commit()
    mydb.close()
    return profile(request)
    
    
#doctor viewing patients    
def viewpatients(request):    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient"
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request, 'viewpatients.html',{'drows':row, 'dname':request.session['susername']})

#doctor sorting the age of patients in view page 
def sortage(request):    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient order by age asc"
    mycursor.execute(q)
    rows=mycursor.fetchall()
    mydb.close()
    return render(request, 'viewpatients.html',{'drows':rows})

#doctor sorting the disease of patients in view page  
def sortdisease(request):    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient order by disease asc"
    mycursor.execute(q)
    rows=mycursor.fetchall()
    mydb.close()
    return render(request, 'viewpatients.html',{'drows':rows})

#doctor sorting the district of patients in view page
def sortdistrict(request):    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient order by district asc"
    mycursor.execute(q)
    rows=mycursor.fetchall()
    mydb.close()
    return render(request, 'viewpatients.html',{'drows':rows})    

#doctor sorting the name of patients in view page
def sortname(request):    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient order by name asc"
    mycursor.execute(q)
    rows=mycursor.fetchall()
    mydb.close()
    return render(request, 'viewpatients.html',{'drows':rows})       
    
#_______________________________________________________________________________________________________________    
    
    
    
#ADMIN

#admin login page
def adminlogin(request):
    return render(request, 'adminlogin.html')

#admin login handler 
def adminloginhandler(request):
    a=request.GET.get("username")
    b=request.GET.get("pass")
    print(a)
    print(b)
    if(a=="admin" and b=="admin"):
        return render(request, 'adminhome.html')
    else:
        return render(request, 'adminlogin.html', {'message':'Invalid Credentials'})



#admin home page
def adminhome(request):
    return render(request, 'adminhome.html')
    
    
#admin viewing doctors
def doctors(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from doc"
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request, 'doctors.html',{'drows':row, 'dname':request.session['susername']})
    
#admin deleting doctor from view page 
def doctordeletehandler(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    a=request.GET.get("selectedid")
    q="delete from doc where docid="+a
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return doctors(request) 
    
    
#admin viewing patients
def patients(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient"
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request, 'patients.html',{'drows':row, 'dname':request.session['susername']})

#admin deleting patient from view page     
def patientdeletehandler(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    a=request.GET.get("selectedid")
    q="delete from patient where patientid="+a
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return patients(request) 


#_______________________________________________________________________________________________________________ 


 
#PATIENT
 
 #patient registration 
def patientregistration(request):
    return render(request, 'patientregistration.html') 

#patient registration handler 
def patientregisterhandler(request):
    a=request.POST.get("name")
    b=request.POST.get("age")
    c=request.POST.get("gender")
    d=request.POST.get("disease")
    e=request.POST.get("district")
    f=request.POST.get("email")
    g=request.POST.get("phone")
    h=request.POST.get("username")
    i=request.POST.get("password")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="insert into patient (name,age,gender,disease,district,email,phone,username,password) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+i+"')"
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return render(request, 'patientregistration.html')

    
#patient login
def patientlogin(request):
    return render(request, 'patientlogin.html')

#patient login handler
def patientloginhandler(request):
    a=request.GET.get("username")
    b=request.GET.get("pass")
    print(a)
    print(b)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from patient where username='"+a+"' and password='"+b+"'"
    mycursor.execute(q)
    row=mycursor.fetchone()
    if row!=None:
     request.session['susername']=a
     request.session['patientno']=row[0]
     return render(request, 'patienthome.html',{'pname':a})
    else:
     return render(request, 'patientlogin.html',{'msg':'Invalid Credential'})



#patient home page
def patienthome(request):
    return render(request, 'patienthome.html',{'pname':request.session['susername']})       


#patient profile page
def patientprofile(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    s=request.session['patientno']
    q="select * from patient where patientid="+str(s)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request, 'patientprofile.html',{'pname':request.session['susername'], 'drows':row}) 

#patient profile update, edit handler
def patientprofileupdatehandler(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    a=request.POST.get("email")
    b=request.POST.get("phone")
    c=request.POST.get("pass")
    d=request.session['patientno']
    q="update patient set password='"+c+"', email='"+a+"', phone='"+b+"' where patientid="+str(d)
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.commit()
    mydb.close()
    return patientprofile(request)
    

#viewing doctors     
def patientsdoctors(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from doc"
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request, 'patientsdoctors.html',{'pname':request.session['susername'],'drows':row}) 

#viewing doctors and getting apppointment
def doctorappointmenthandler(request):
    a=request.GET.get("selectedid")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    mycursor=mydb.cursor()
    q="select * from doc where docid="+a
    mycursor.execute(q)
    row=mycursor.fetchone()
    mydb.close()
    return render(request, 'doctorappointment.html',{'drows':row, 'dname':request.session['susername']})    

def doctorappointmentconfirmation(request):
        a=request.POST.get("doctorid")
        b=request.POST.get("doctorname")
        c=request.POST.get("atime")
        d=request.POST.get("adate")
        e=request.POST.get("token")
        f=str(request.session['patientno'])
        g=request.session['susername']
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mydb.cursor()
        q="insert into appoinment (doctorid,doctorname,time,date,token,patientid,patientname) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"', '"+f+"', '"+g+"')"
        print(q)
        mycursor.execute(q)
        mydb.commit()
        mydb.close()
        return patientsdoctors(request)
        
def trackappointment(request):
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        mycursor=mydb.cursor()
        s=request.session['patientno']
        q="select * from appoinment where patientid="+str(s)
        mycursor.execute(q)
        row=mycursor.fetchall()
        mydb.close()
        return render(request, 'trackappointment.html',{'pname':request.session['susername'],'drows':row}) 
    
       
        
        
        

#_______________________________________________________________________________________________________________
