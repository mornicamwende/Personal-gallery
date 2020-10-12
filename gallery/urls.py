from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
    url(r'^$', views.welcome, name='welcome'),
    # url('^$',views.gallery,name = 'gallery'),
    url(r'^location/(\d+)',views.location,name = 'location'),
    url(r'^search/',views.search,name='search')    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)