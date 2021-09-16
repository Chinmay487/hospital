from django.shortcuts import render,redirect
from django.views import View
from . import forms
from patient.models import Patient_details,Appointments
from django.contrib.auth.models import auth,User


class Home(View):
    def get(self,request):
        content = {
            'page_title' : 'Home Page',
            'details':Patient_details.objects.all()[::-1]
        }
        return render(request,'index.html',content)


class Today_appointments(View):
    def get(self,request):
        if request.user.is_authenticated:
            content = {
                'page_title' : "today's Appointments",
                'appointments' : Appointments.objects.all()[::-1]
            }
            page = 'view_appointments.html'
        else:
            content = {
                'page_title':'Page not found',
            }
            page = '404.html'
            
        return render(request,page,content)

class Login_Page(View):
    def get(self,request):
        content = {
            'page_title' : 'Login Page',
            'login_form' : forms.Login_form
        }
        return render(request,'login.html',content)

    def post(self,request):
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username = user_name,password = password)
        if user is not None:
            auth.login(request,user)

        return redirect('/')

class Logout_Page(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')



