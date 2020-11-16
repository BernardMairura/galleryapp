from django.urls import path,re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('', views.my_images, name='my_images'),
    
    path('search/', views.search_results, name='search_results'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.previous_days_photos,name = 'previousPhotos'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    