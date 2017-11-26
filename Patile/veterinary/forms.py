from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Kullanıcı Adı", help_text="",
                               widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı'}))

    password = forms.CharField(label='Parola:',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Parola'}))

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_password(self):
        return self.password

    def clean_username(self):
        return self.username
