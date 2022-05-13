from apps.dictionary.views import WordDetailView, WordCreateView, WordUpdateView, WordSearchView
from django.urls import path

app_name = 'dictionary'
urlpatterns = [
    path('add_new/', WordCreateView.as_view(), name='word-create'),
    path('search/', WordSearchView.as_view(), name='word-search'),
    path('<str:pk>/update/', WordUpdateView.as_view(), name='word-update'),
    path('<str:pk>/', WordDetailView.as_view(), name='word-detail'),
]
