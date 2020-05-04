from django import forms
from .models import Posts
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class PostForm(forms.ModelForm):
    name = forms.CharField(label=_("post_title_field"),
                           required=True)
    # tags = forms.CharField(label=_("post_tags_field"),
    #                        required=False)
    post = forms.CharField(label=_("post_body_field"),
                           required=True, widget=SummernoteWidget({'width': '100%', 'height': '600px'}))

    class Meta:
        model = Posts
        fields = ('name', 'post')


class PostSearchForm(forms.Form):
    name = forms.CharField(
        label=_("post_title_field"),
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
