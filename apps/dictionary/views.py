from apps.dictionary.forms import WordCreateForm, WordUpdateForm
from apps.dictionary.models import Word
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView


class WordDetailView(DetailView):
    model = Word
    template_name = 'dictionary/word_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word = context['word']
        context['parts_of_speech'] = word.get_parts_of_speech()

        return context


class WordCreateView(CreateView):
    model = Word
    form_class = WordCreateForm
    template_name = 'dictionary/word_create.html'
    success_url = reverse_lazy('dictionary:word-create')


class WordUpdateView(UpdateView):
    model = Word
    form_class = WordUpdateForm
    template_name = 'dictionary/word_update.html'
    success_url = reverse_lazy('dictionary:main')
