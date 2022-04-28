from dictionary.models import Word
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Button, Div, Field, Submit


class WordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'word',
            Div('adjective', id='hide_adjective', style='display: none'),
            Div('adverb', id='hide_adverb', style='display: none'),
            Div('conjunction', id='hide_conjunction', style='display: none'),
            Div('interjection', id='hide_interjection', style='display: none'),
            Div('noun', id='hide_noun', style='display: none'),
            Div('preposition', id='hide_preposition', style='display: none'),
            Div('pronoun', id='hide_pronoun', style='display: none'),
            Div('verb', id='hide_verb', style='display: none'),
            Div(Submit('save', 'Save'), Button('cancel', 'Cancel'), css_class='d-flex justify-content-end')
        )

    class Meta:
        model = Word
        fields = '__all__'


class WordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div('adjective', id='hide_adjective', style='display: none'),
            Div('adverb', id='hide_adverb', style='display: none'),
            Div('conjunction', id='hide_conjunction', style='display: none'),
            Div('interjection', id='hide_interjection', style='display: none'),
            Div('noun', id='hide_noun', style='display: none'),
            Div('preposition', id='hide_preposition', style='display: none'),
            Div('pronoun', id='hide_pronoun', style='display: none'),
            Div('verb', id='hide_verb', style='display: none'),
            Div(Submit('save', 'Save', onclick='clearInput()'), Button('cancel', 'Cancel'), css_class='d-flex justify-content-end')
        )

    class Meta:
        model = Word
        exclude = ['word']
