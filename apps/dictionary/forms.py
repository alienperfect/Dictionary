from apps.dictionary.models import Word
from django import forms


class WordCreateForm(forms.ModelForm):
    adjective = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    adverb = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    conjunction = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    interjection = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    noun = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    preposition = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    pronoun = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    verb = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Word
        fields = '__all__'


class WordUpdateForm(forms.ModelForm):
    adjective = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    adverb = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    conjunction = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    interjection = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    noun = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    preposition = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    pronoun = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    verb = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Word
        exclude = ['word']
