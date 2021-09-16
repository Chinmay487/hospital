from django import forms

class Patient_form(forms.Form):
    patient_name = forms.CharField(max_length = 50)
    contact = forms.CharField(max_length = 10)
    admission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ward_number = forms.IntegerField()
    total_payment = forms.IntegerField()
    disease = forms.CharField(max_length = 50)


class Update_form(Patient_form):
    patient_name = forms.CharField(required = False)
    contact = forms.CharField(required = False)
    admission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required = False)
    ward_number = forms.IntegerField(required = False)
    total_payment = forms.IntegerField(required = False)
    disease = forms.CharField(required = False)
    discharge = forms.BooleanField(required = False)

class Appointment_form(forms.Form):
    patient_name = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=10)
    disease = forms.CharField(max_length=50)
    email = forms.EmailField()
    date_for_appointment = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))