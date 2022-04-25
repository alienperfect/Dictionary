from dictionary.models import Word
from django import forms


class WordCreateForm(forms.ModelForm):
    adjective = forms.CharField(help_text='Provide definition.', required=False)
    adverb = forms.CharField(help_text='Provide definition.', required=False)
    conjunction = forms.CharField(help_text='Provide definition.', required=False)
    interjection = forms.CharField(help_text='Provide definition.', required=False)
    noun = forms.CharField(help_text='Provide definition.', required=False)
    preposition = forms.CharField(help_text='Provide definition.', required=False)
    pronoun = forms.CharField(help_text='Provide definition.', required=False)
    verb = forms.CharField(help_text='Provide definition.', required=False)

    class Meta:
        model = Word
        fields = '__all__'


class WordUpdateForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
