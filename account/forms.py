from account.models import Collection
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Button, Div, Field, Submit


class CollectionCreateForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ['user']


class CollectionUpdateForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ['user']
