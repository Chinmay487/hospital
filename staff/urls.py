from django.urls import path
from . import views
from patient.views import New_patient,Details,Update_info,Book_appointment

urlpatterns = [
    path('',views.Home.as_view(),name="Home"),
    path('login',views.Login_Page.as_view(),name="login"),
    path('logout',views.Logout_Page.as_view(),name="logout"),
    path('new_patient',New_patient.as_view(),name="new_patient"),
    path('details/',Details.as_view(),name="details"),
    path('update/',Update_info.as_view(),name='update_info'),
    path('book_appointment',Book_appointment.as_view(),name="book_appointment"),
    path('view_appointment',views.Today_appointments.as_view(),name="todays_appointments")
]