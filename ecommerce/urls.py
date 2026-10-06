import django
from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from ecom.views import custom_404_view

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)
handler404 = custom_404_view

urlpatterns = [
    path("404/", custom_404_view),
    path("500/", custom_server_error),
    path('', views.home_view, name=''),
    path('api/contact/', views.contact, name='contact')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)