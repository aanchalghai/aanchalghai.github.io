from django import forms
from django.contrib.auth import get_user_model
from .validators import vpassword,validate_email_unique



# Create your forms here.
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                             'id':'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                           'id':'email'}),
                                                            validators=[validate_email_unique])
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'id':'password'}),
                                                                validators=[vpassword])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'id':'password'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')
