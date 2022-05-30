from apps.dictionary.forms import WordCreateForm, WordUpdateForm
from apps.dictionary.models import Word
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, TemplateView


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


class WordSearchView(ListView):
    model = Word
    template_name = 'dictionary/word_search_result.html'

    def search(self):
        query = self.request.GET.get('q', '')
        word_list = Word.objects.filter(word__icontains=query)
        return {'word_list': word_list, 'query': query}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word_list'] = self.search().get('word_list')
        return context

    def get(self, request, *args, **kwargs):
        """If input matches word, redirect to DetailView."""
        query = self.search().get('query')
        word_list = self.search().get('word_list')

        try:
            if query == word_list.first().pk:
                return HttpResponseRedirect(reverse_lazy('dictionary:word-detail', kwargs={'pk': query}))
        except:
            return super().get(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)
