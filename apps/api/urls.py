from apps.api.views import WordAPIView, WordListAPIView, CollectionAPIView
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('word/<str:word>/', WordAPIView.as_view(), name='word'),
    path('words/<str:entry>', WordListAPIView.as_view(), name='words'),
    path('collection/<int:pk>/', CollectionAPIView.as_view(), name='collection'),
]
