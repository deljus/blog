from .models import Profile
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    about = forms.CharField(label=_("About"),
                            required=False,
                            widget=forms.Textarea(attrs={"rows": 5,
                                                         "cols": 40,
                                                         "style": "width: 100%"}))

    birth_date = forms.DateField(label=_("Birth date"),
                                 required=False,
                                 widget=forms.DateInput(format='%d/%m/%Y',
                                                        attrs={'class': 'col-md-12 form-control',
                                                               'placeholder': 'DD/MM/YYYY',
                                                               'id': 'birth-date-picker'}))

    avatar = forms.ImageField(label=_("Avatar"), required=False)

    class Meta:
        model = Profile
        fields = ("about", "birth_date", "avatar")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))

    email = forms.EmailField(required=True,
                             label='Email')

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")