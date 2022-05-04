from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


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
