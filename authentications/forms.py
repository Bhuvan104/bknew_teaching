from django import forms
from django.forms import ValidationError

class RegisterForm(forms.Form):
    first_name =  forms.CharField(label='First name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your First name"}))
    last_name =  forms.CharField(label='Last name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your Last Name"}))
    email =  forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your Email"}))
    password =  forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your Password"}))
    # confirm_password =  forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your Confirm Password"}))
    # image =  forms.CharField(label='Upload your profile',widget=forms.FileInput(attrs={'class':'form-control'}))
    
    def clean_first_name(self,**args):
            title = self.cleaned_data.get('first_name')
            if title is None:
                raise forms.ValidationError("The field is not empty")