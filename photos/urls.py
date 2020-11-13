from django.urls import path,re_path
from .import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('^today/$',views.photos_of_day,name='photosToday'),
    # re-path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.previous_days_photos,name = 'previousPhotos'),
]


    