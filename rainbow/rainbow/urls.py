
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('events/',views.events,name="events"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('mail/',views.mail,name="mail"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)