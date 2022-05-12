from apps.account.models import Collection
from django import forms


class CollectionCreateForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ['user']


class CollectionUpdateForm(forms.ModelForm):
    class Meta:
        model = Collection
        exclude = ['user']
