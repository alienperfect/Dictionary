from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include('apps.api.urls', namespace='api')),
    path('definition/', include('apps.dictionary.urls', namespace='dictionary')),
    path('account/', include('apps.account.urls', namespace='account')),
]
