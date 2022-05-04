from account.views import SignUpView, CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

app_name = 'account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('dictionary:main')), name='logout'),
]
