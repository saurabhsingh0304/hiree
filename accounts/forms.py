from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfile
from django.contrib.auth import authenticate

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(
#         max_length=60, help_text='Required. Add a valid email address')

#     class Meta:
#         model = UserProfile
#         fields = ('email', 'password1', 'password2', )


# class UserAuthenticationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     class Meta:
#         model = UserProfile
#         fields = ('email', 'password')

#     def __init__(self, *args, **kwargs):
#         """
#           specifying styles to fields 
#         """
#         super(UserAuthenticationForm, self).__init__(*args, **kwargs)
#         for field in (self.fields['email'], self.fields['password']):
#             field.widget.attrs.update({'class': 'form-control '})

#     def clean(self):
#         if self.is_valid():
#             email = self.cleaned_data.get('email')
#             password = self.cleaned_data.get('password')
#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError('Invalid Login')
