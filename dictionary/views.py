from dictionary.forms import WordCreateForm
from dictionary.models import Word
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView


class WordDetailView(DetailView):
    model = Word
    template_name = 'dictionary/word_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        parts_of_speech = (
            'adjective',
            'adverb',
            'conjunction',
            'interjection',
            'noun',
            'preposition',
            'pronoun',
            'verb'
            )

        word = context['word']
        context['part_of_speech'] = [part for part in parts_of_speech if hasattr(word, part)]

        return context

    def get_object(self):
        word = self.kwargs['word']

        return get_object_or_404(Word, word=word)


class WordCreateView(CreateView):
    model = Word
    form_class = WordCreateForm
    template_name = 'dictionary/word_create.html'
    success_url = reverse_lazy('dictionary:main')
