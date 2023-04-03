from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import permission_required

from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',permission_required('ads.can_add_ad')(
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all'))), name='ad_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('article/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined