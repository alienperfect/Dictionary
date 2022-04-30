from api.views import ApiWord
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('word/<str:word>/', ApiWord.as_view(), name='word'),
]
