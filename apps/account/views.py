from apps.account.forms import CollectionCreateForm, CollectionUpdateForm
from apps.account.models import Collection
from apps.dictionary.models import Word
from django.contrib.auth import login, get_user
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'

    def form_valid(self, form):
        """Saves the model and logs the user in."""
        form.save()
        login(self.request, form.instance)

        return HttpResponseRedirect('/')


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    next_page = '/'
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

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'account/collection_detail.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', '')
        try:
            user = Collection.objects.get(pk=pk).user
            if user != get_user(request):
                raise Http404()
        except ObjectDoesNotExist:
            raise Http404()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        instance = context.get('object')
        context['words'] = Word.objects.filter(collection=instance)
        return context


def collection_delete_redirect(request, **kwargs):
    return HttpResponseRedirect(reverse_lazy('account:collection-list'))
