from django.shortcuts import render,redirect
from django.views import View
from . import forms
from patient.models import Patient_details


class Home(View):
    def get(self,request):
        content = {
            'page_title' : 'Home Page',
            'details':Patient_details.objects.all()[::-1]
        }
        return render(request,'index.html',content)


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
        print(user_name,password)
        return redirect('/')

class Logout_Page(View):
    def get(self,request):
        return redirect('/')



