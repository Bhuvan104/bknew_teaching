from django import forms
from django.forms import ValidationError

class RegisterForm(forms.Form):
    first_name =  forms.CharField(label='First name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your First name"}))
    last_name =  forms.CharField(label='Last name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your Last Name"}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')],widget=forms.Select(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    image =  forms.ImageField()
    email =  forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your Email"}))
    password =  forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your Password"}))
    confirm_password =  forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your Confirm Password"}))
    role =  forms.CharField(label='',initial='3',widget=forms.HiddenInput(attrs={'class':'form-control','placeholder':"Enter your Last Name"}))
   
    
    def clean_first_name(self,**args):
            title = self.cleaned_data.get('first_name')
            if title is None:
                raise forms.ValidationError("The field is not empty")
            
    
    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data