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
                                                               'id': 'birth-date-picker'}))

    avatar = forms.ImageField(
        label=_("Avatar"),
        required=False,
        widget=forms.FileInput()
    )

    class Meta:
        model = Profile
        fields = ("about", "birth_date", "avatar")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SignupForm(UserCreationForm):
    username = forms.CharField(label=_('username'),
                               widget=forms.TextInput(attrs={'autofocus': True}))

    email = forms.EmailField(required=True,
                             label=_('email'))

    password1 = forms.CharField(
        label=_("password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("password_confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserSearchForm(forms.Form):
    username = forms.CharField(
        label=_("username"),
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    first_name = forms.CharField(
        label=_("first_name"),
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    last_name = forms.CharField(
        label=_("last_name"),
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
