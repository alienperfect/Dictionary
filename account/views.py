from account.forms import CollectionCreateForm, CollectionUpdateForm
from account.models import Collection
from dictionary.models import Word
from django.contrib.auth import login, get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'

    def form_valid(self, form):
        """Saves the model and logs the user in."""
        form.save()
        login(self.request, form.instance)

        return HttpResponseRedirect(reverse_lazy('dictionary:main'))


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    next_page = reverse_lazy('dictionary:main')
    redirect_authenticated_user = True


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionCreateForm
    template_name = 'account/collection_create.html'
    success_url = reverse_lazy('account:collection-list')

    def form_valid(self, form):
        form.instance.user = get_user(self.request)

        return super().form_valid(form)


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionUpdateForm
    template_name = 'account/collection_update.html'
    success_url = reverse_lazy('account:collection-list')

    def form_valid(self, form):
        form.instance.user = get_user(self.request)

        return super().form_valid(form)


class CollectionListView(ListView):
    model = Collection
    template_name = 'account/collection_list.html'
    context_object_name = 'collections'
    ordering = ['name']


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'account/collection_detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        instance = context.get('object')
        context['words'] = Word.objects.filter(collection=instance)

        return context
