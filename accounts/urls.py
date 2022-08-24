from django.urls import path
from accounts.views import register
from accounts.views import doctor_register
from accounts.views import patient_register,doctor_login_request,logout_view,doctor_details,patient_details,patient_login_request,addblog
from accounts.views import showblogs,blogDetail,showdoctors,addappointment,AppointmentDetail
urlpatterns=[

        path('register/',register,name='register'),
        path('doc_reg/',doctor_register.as_view(),name='doc_reg'),
        path('pat_reg/',patient_register.as_view(),name='pat_reg'),
        path('doc_login/doc_details/<int:pk>/',doctor_details.as_view(),name='docdetails'),
        path('pat_login/pat_details/<int:pk>/',patient_details.as_view(),name='patdetails'),
        path('doc_login/',doctor_login_request, name='doctorlogin'),
        path('pat_login/',patient_login_request, name='patientlogin'),
        path('logout/',logout_view, name='logout'),
        path('addblog/',addblog, name='addblog'),
        path('addappointment/',addappointment, name='addappointment'),
        path('showblogs/',showblogs.as_view(), name='showblogs'),
        path('blog/<int:pk>/',blogDetail.as_view(), name='blog'),
        path('addappointment/appointment/<int:pk>/',AppointmentDetail.as_view(), name='appointment'),
        path('showdoctors/',showdoctors.as_view(), name='showdoctors'),


]
