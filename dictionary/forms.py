from dictionary.models import Word
from django import forms


class WordCreateForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
