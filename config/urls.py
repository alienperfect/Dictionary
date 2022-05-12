from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls', namespace='api')),
    path('definition/', include('apps.dictionary.urls', namespace='dictionary')),
    path('account/', include('apps.account.urls', namespace='account')),
]
