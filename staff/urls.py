from django.urls import path
from . import views
from patient.views import New_patient,Details,Update_info

urlpatterns = [
    path('',views.Home.as_view(),name="Home"),
    path('login',views.Login_Page.as_view(),name="login"),
    path('logout',views.Logout_Page.as_view(),name="logout"),
    path('new_patient',New_patient.as_view(),name="new_patient"),
    path('details/',Details.as_view(),name="details"),
    path('update/update',Update_info.as_view(),name='update_info'),
    path('update/',Update_info.as_view(),name='update_info')
    # path(r'^update/(?P<patient_id>\d+)/$',Update_info.as_view(),name='update_info')
]