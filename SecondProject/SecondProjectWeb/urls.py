from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('home', views.home, name='home'),
path('registration', views.registration, name='registration'),
path('registerhandler', views.registerhandler, name='registerhandler'),
path('doctorlogin', views.doctorlogin, name='doctorlogin'),
path('loginhandler', views.loginhandler, name='loginhandler'),
path('doctorhome', views.doctorhome, name='doctorhome'),
path('profile', views.profile, name='profile'),
path('profileupdatehandler', views.profileupdatehandler, name='profileupdatehandler'),
path('patientprofileupdatehandler', views.patientprofileupdatehandler, name='patientprofileupdatehandler'),
path('patientprofile', views.patientprofile, name='patientprofile'),
path('patientlogin', views.patientlogin, name='patientlogin'),

path('doctorappointmentconfirmation', views.doctorappointmentconfirmation, name='doctorappointmentconfirmation'),
path('patientregistration', views.patientregistration, name='patientregistration'),
path('adminlogin', views.adminlogin, name='adminlogin'),
path('adminhome', views.adminhome, name='adminhome'),
path('patients', views.patients, name='patients'),
path('doctors', views.doctors, name='doctors'),

path('doctorappointmenthandler', views.doctorappointmenthandler, name='doctorappointmenthandler'),
path('adminloginhandler', views.adminloginhandler, name='adminloginhandler'),

path('patientloginhandler', views.patientloginhandler, name='patientloginhandler'),
path('patientregisterhandler', views.patientregisterhandler, name='patientregisterhandler'),

path('patientprofileupdatehandler', views.patientprofileupdatehandler, name='patientprofileupdatehandler'),
path('patientdeletehandler', views.patientdeletehandler, name='patientdeletehandler'),
path('doctordeletehandler', views.doctordeletehandler, name='doctordeletehandler'),

path('patienthome', views.patienthome, name='patienthome'),
path('patientsdoctors', views.patientsdoctors, name='patientsdoctors'),
path('viewpatients', views.viewpatients, name='viewpatients'),
path('viewappointments', views.viewappointments, name='viewappointments'),
path('trackappointment', views.trackappointment, name='trackappointment'),
#path('approvehandler', views.approvehandler, name='approvehandler'),

path('sortage', views.sortage, name='sortage'),
path('sortdisease', views.sortdisease, name='sortdisease'),
path('sortdistrict', views.sortdistrict, name='sortdistrict'),
path('sortname', views.sortname, name='sortname'),
]

