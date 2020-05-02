from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import profile ,profile_update


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
           model = User
           fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ['username','email']
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = profile
        fields =['image']
    
class profileUpdateForms(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    present_address = forms.CharField(label='Present Addres')
    perment_address = forms.CharField(label='perment Addres')
    bio = forms.CharField(label='Bio')
    birthday =forms.DateField(label='Birthday')
    contact =forms.CharField(label='contact')
    class Meta():
        model = profile
        fields = ['first_name','last_name','present_address','perment_address','bio','birthday','image']