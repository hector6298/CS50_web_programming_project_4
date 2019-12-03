from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, SkinImages

class UserRegistration(UserCreationForm):
    age = forms.IntegerField(max_value=110, min_value=0)
    bloodType = forms.ChoiceField(choices=Patient.BLOOD_TYPES)
    height = forms.DecimalField(max_digits=3, decimal_places=2)
    weight = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']
    
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Cannot create user without saving to database")
        user = super(UserRegistration, self).save(commit=True)
        patient = Patient(user=user, age=self.cleaned_data['age'],
                            bloodType=self.cleaned_data['bloodType'],
                            height=self.cleaned_data['height'],
                            weight=self.cleaned_data['weight'])
        patient.save()
        return user


class ImageUpload(forms.ModelForm):

    class Meta:
        model = SkinImages
        fields = ['title', 'image']
    
