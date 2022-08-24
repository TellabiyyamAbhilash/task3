
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models import Doctor,Patient,User,Blog,Appointment
from django import forms

class DoctorSignupForm(UserCreationForm):
    FirstName = forms.CharField(required=True)
    LastName = forms.CharField(required=True)
    profilepicture  = forms.ImageField(required=False)
    Address_line1 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    last_login = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model=User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.FirstName = self.cleaned_data.get('FirstName')
        doctor.LastName = self.cleaned_data.get('LastName')
        doctor.profilepicture  = self.cleaned_data.get('profilepicture')
        doctor.Address_line1 = self.cleaned_data.get('Address_line1')
        doctor.city = self.cleaned_data.get('city')
        doctor.state = self.cleaned_data.get('state')
        doctor.pincode = self.cleaned_data.get('pincode')
        doctor.last_login = self.cleaned_data.get('last_login')
        doctor.save()
        return user

class PatientSignupForm(UserCreationForm):
    FirstName = forms.CharField(required=True)
    LastName = forms.CharField(required=True)
    profilepicture  = forms.ImageField(required=False)
    Address_line1 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    last_login = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model=User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.FirstName = self.cleaned_data.get('FirstName')
        patient.LastName = self.cleaned_data.get('LastName')
        patient.profilepicture  = self.cleaned_data.get('profilepicture')
        patient.Address_line1 = self.cleaned_data.get('Address_line1')
        patient.city = self.cleaned_data.get('city')
        patient.state = self.cleaned_data.get('state')
        patient.pincode = self.cleaned_data.get('pincode')
        patient.last_login = self.cleaned_data.get('last_login')
        patient.save()
        return user

class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['title','image','category','summary','content']
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'image':forms.FileInput(attrs={'class':'form-control'}),
                'category':forms.Select(attrs={'class':'form-control'}),
                'summary':forms.TextInput(attrs={'class':'form-control'}),
                'content':forms.TextInput(attrs={'class':'form- control'})
        }

class Appointment_Form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields=['speciality','date','doctor','time']
        widgets = {
                'speciality':forms.TextInput(attrs={'class':'form-control'}),
                'doctor':forms.Select(attrs={'class':'form-control'}),
                'date':forms.DateInput(),
                'time':forms.TimeInput()
        }
