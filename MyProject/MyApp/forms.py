from django import forms
from django.contrib.auth.models import User
from MyApp.models import UserProfileInfo

class SignUp(forms.ModelForm):
    # Form Fields go here
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify email:')
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("make sure emails match!")


    class Meta:
        model = User
        fields = "__all__"
        ## exclude = ["field1", "field2"]
        ## fields = ("fields1" "fields2")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_picture')