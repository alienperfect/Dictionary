from apps.account.views import SignUpView, CustomLoginView, CollectionListView, CollectionCreateView, CollectionUpdateView, CollectionDetailView
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

app_name = 'account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('collection/add_new/', CollectionCreateView.as_view(), name='collection-create'),
    path('collection/<int:pk>/update/', CollectionUpdateView.as_view(), name='collection-update'),
    path('collections/', CollectionListView.as_view(), name='collection-list'),
    path('collection/<int:pk>/', CollectionDetailView.as_view(), name='collection-detail'),
]
