from django.urls import path
from dictionary.views import WordDetailView, WordCreateView, WordUpdateView
from django.views.generic import TemplateView

app_name = 'dictionary'
urlpatterns = [
    path('', TemplateView.as_view(template_name='dictionary/index.html'), name='main'),
    path('add_new/', WordCreateView.as_view(), name='word-create'),
    path('<str:word>/update/', WordUpdateView.as_view(), name='word-update'),
    path('<str:word>/', WordDetailView.as_view(), name='word-detail'),
]
