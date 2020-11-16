from django.urls import path,re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('', views.my_images, name='my_images'),
    
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'image_details/(?P<image_id>[0-9]+)/$', views.image_details, name='image_details'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    