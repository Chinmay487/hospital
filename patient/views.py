from django.shortcuts import render,redirect
from django.views import View
from . import forms
from . import models


class New_patient(View):
    def get(self,request):
        content = {
            'page_title' : 'Add new Patient',
            'patient_form':forms.Patient_form()
        }
        return render(request,'new_patient.html',content)

    def post(self,request):
        patient_name = request.POST['patient_name']
        contact = request.POST['contact']
        disease = request.POST['disease']
        admission_date = request.POST['admission_date']
        ward_number = request.POST['ward_number']
        total_payment = request.POST['total_payment']
        
        new_patient = models.Patient_details(
            patient_name = patient_name,
            contact = contact,
            disease = disease,
            admission_date = admission_date,
            ward_number = ward_number,
            total_payment = total_payment
            )
        new_patient.save()
        return redirect('/')


class Details(View):
    def get(self,request):
        patient_id = request.GET['patient_id']
        content = {
            'page_title' : 'Patient Details',
            'patient_detail':models.Patient_details.objects.get(id = patient_id)
        }
        return render(request,'details.html',content)


class Update_info(View):
    def get(self,request):
        patient_id = request.GET['patient_id']
        content = {
            'page_title':'Update details',
            'current_details':models.Patient_details.objects.get(id = patient_id),
            'update_form':forms.Update_form()
        }
        return render(request,'update_info.html',content)

    def post(self,request):
        patient_id = request.POST['patient_id']
        disease = request.POST['disease']
        ward_number = request.POST['ward_number']
        total_payment = request.POST['total_payment']
        admission_date = request.POST['admission_date']
        got_discharge = request.POST.get('got_discharge',False)
        print(got_discharge)
        
        current_info = models.Patient_details.objects.get(id = patient_id)
        
        current_info.disease = current_info.disease if disease == '' else disease
        current_info.ward_number = current_info.ward_number if ward_number == '' else ward_number
        current_info.total_payment  = current_info.total_payment if total_payment == '' else current_info.total_payment+eval(total_payment)
        current_info.admission_date  = current_info.admission_date if admission_date == '' else admission_date
        current_info.got_discharge = got_discharge
        current_info.save()

        return redirect('/')






